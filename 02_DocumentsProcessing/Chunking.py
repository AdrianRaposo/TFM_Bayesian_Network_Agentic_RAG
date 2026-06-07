import tiktoken
import re
import unicodedata
import html
import os
import json
import traceback
import time

from LoggerSetUp import setup_logger
from pathlib import Path
from typing import List, Tuple, Dict, Iterable



from config import(
    CLEANED_DATA_PATH_MD,
    CHUNKING_IMPROVED_OUTPUT_DIR,
    SYMBOL_MAP,
    TIKTOKEN_MODEL_FOR_COUNT,
    LOGS_BASE_PATH,
    LOG_LEVEL,
    FORMULA_BLOCK_PATTERN,
    FORMULA_INLINE_PATTERN,
    CODE_BLOCK_FENCE_PATTERN,
    CODE_INLINE_PATTERN,
    IMAGE_MD_PATTERN,
    TABLE_PATTERN,
    DATA_BLOCK_PATTERN,
    HEADER_SPLIT_RE,
    LOW_VALUE_PATTERNS,
    CHUNK_MIN_TOKENS,
    CHUNK_MAX_TOKENS,
    CHUNK_OVERLAP_FRAC,
    SENTENCE_SPLIT_RE
)

# Configure logger
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='Chunking.log',
    error_log_filename='Chunking_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)

# Tokenizer for counting tokens
_TKT_ENC = tiktoken.encoding_for_model(TIKTOKEN_MODEL_FOR_COUNT)

def count_tokens(text: str) -> int:
    """
    Counts tokens using tiktoken (configurable model).
    If tiktoken is not available, uses approximation of ~4 chars/token.

    Args:
        text (str): The input text to count tokens for.
    Returns:
        int: The number of tokens in the input text.
    """
    if not text:
        return 0
    if not _TKT_ENC:
        # Fallback approximation
        return max(1, len(text) // 4)
    
    return len(_TKT_ENC.encode(text or ""))

def iter_markdown_files(input_dir: str) -> Iterable[Path]:
    """
    Returns all .md files under input_dir, recursively.

    Args:
        input_dir (str): The directory to search for .md files.
    Yields:
        Iterable[Path]: An iterable of Path objects for each .md file found.
    """
    base = Path(input_dir)
    for p in base.rglob("*.md"):
        if p.is_file():
            yield p

#--- Text cleaning functions ---
def extract_and_protect_formulas(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Replaces LaTeX formulas with placeholders [FORMULA_i] and returns:
    - text with placeholders
    - map { "[FORMULA_i]": original_latex }
    Args:
        text (str): Input text that may contain LaTeX formulas.
    Returns:
        Tuple[str, Dict[str, str]]: Text with placeholders and formula map.  
    """
    formulas: Dict[str, str] = {}
    idx = 0

    def _sub_block(m):
        nonlocal idx
        placeholder = f"[FORMULA_{idx}]"
        formulas[placeholder] = m.group(0)
        logger.debug(f"Extracted block formula: {placeholder} -> {m.group(0)[:30]}...")
        idx += 1
        return placeholder

    def _sub_inline(m):
        nonlocal idx
        placeholder = f"[FORMULA_{idx}]"
        formulas[placeholder] = m.group(0)
        logger.debug(f"Extracted inline formula: {placeholder} -> {m.group(0)[:30]}...")
        idx += 1
        return placeholder

    # First block formulas $$...$$ (greedy DOTALL)
    text = re.sub(FORMULA_BLOCK_PATTERN, _sub_block, text, flags=re.DOTALL)
    logger.debug(f"Extracted {len(formulas)} block formulas")
    # Then inline $...$
    text = re.sub(FORMULA_INLINE_PATTERN, _sub_inline, text)
    logger.debug(f"Extracted {len(formulas)} total formulas (including inline)")
    return text, formulas

def extract_and_placeholder_code(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Replaces code blocks (```...```) and inline code (`...`) with [CODE_k].
    Returns:
    - text with placeholders
    - map { "[CODE_k]": original_content }
    Args:
        text (str): Input text that may contain code blocks and inline code.   
    Returns:
        Tuple[str, Dict[str, str]]: Text with placeholders and map of code content.
    """
    code: Dict[str, str] = {}
    idx = 0

    # Blocks with triple fences, DOTALL
    def _sub_block(m):
        nonlocal idx
        content = m.group(0)
        placeholder = f"[CODE_{idx}]"
        code[placeholder] = content
        idx += 1
        return placeholder

    text = re.sub(CODE_BLOCK_FENCE_PATTERN, _sub_block, text, flags=re.DOTALL)

    # Inline `...` (no DOTALL)
    def _sub_inline(m):
        nonlocal idx
        content = m.group(0)
        placeholder = f"[CODE_{idx}]"
        code[placeholder] = content
        idx += 1
        return placeholder

    text = re.sub(CODE_INLINE_PATTERN, _sub_inline, text)

    return text, code

def extract_and_protect_tables(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Replaces Markdown tables or tabular blocks with placeholders [TABLE_i] and returns:
    - text with placeholders
    - map { "[TABLE_i]": original_table }

    Args:
        text (str): Input text that may contain Markdown tables or tabular blocks.

    Returns:
        Tuple[str, Dict[str, str]]: Text with placeholders and table map.
    """
    tables: Dict[str, str] = {}
    idx = 0

    def _sub_table(m):
        nonlocal idx
        placeholder = f"[TABLE_{idx}]"
        tables[placeholder] = m.group(0).strip()
        logger.debug(
            f"Extracted table {placeholder}: {m.group(0).splitlines()[0][:30]}..."
        )
        idx += 1
        return placeholder

    # First, detect classic Markdown tables
    new_text = TABLE_PATTERN.sub(_sub_table, text)
    # Then, detect simple tabular blocks
    new_text = DATA_BLOCK_PATTERN.sub(_sub_table, new_text)

    logger.debug(f"Extracted {len(tables)} tables (Markdown + Data blocks)")
    return new_text, tables

def remove_markdown_images(text: str) -> str:
    """
    Removes all Markdown image references ![...](...).
    Args:
        text (str): Input text that may contain Markdown image references.
    Returns:
        str: Text with Markdown image references removed.
    """
    return re.sub(IMAGE_MD_PATTERN, "", text)

def remove_markdown_headers(text: str) -> str:
    """
    Removes Markdown headers (lines starting with #) from the input text.
    Args:
        text (str): Input text that may contain Markdown headers.
    Returns:
        str: Text with Markdown headers removed.
    """

    # Markdown headers (start of line with #+ space)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", text)

    return text

def normalize_unicode_to_ascii(text: str) -> str:
    """
    Robustly normalizes to ASCII: NFKD + removes diacritics.
    If a character is not ASCII after normalization:
      - Tries to replace it using SYMBOL_MAP (or the provided dictionary)
      - If no mapping exists, uses '_'
    Args:
        text (str): Input text to normalize.
    Returns:
        str: Normalized text.
    """
    if not text:
        return text

    norm = unicodedata.normalize("NFKD", text)
    out_chars = []

    for ch in norm:
        # Remove diacritic marks
        if unicodedata.category(ch) == "Mn":
            continue

        try:
            ch.encode("ascii")
            out_chars.append(ch)
        except Exception:
            out_chars.append(SYMBOL_MAP.get(ch, "_"))

    return "".join(out_chars)

def preclean_for_chunking(text: str) -> str:
    """
    Performs basic cleaning of text before chunking:
    - Decodes HTML entities.
    - Removes HTML tags.
    - Converts Markdown links [text](url) to just text.
    - Removes blockquotes, footnote definitions and references.
    - Removes Markdown emphasis (bold, italics).
    - Removes horizontal rules.
    - Strips leading/trailing whitespace.
    - Normalizes Unicode to ASCII (using SYMBOL_MAP for replacements).

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text, ready for chunking.
    """
    # Decode HTML entities if present
    text = html.unescape(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)

    # Blockquotes at start of line
    text = re.sub(r"(?m)^\s*>\s?", "", text)

    # Remove footnote definitions and references
    text = re.sub(r"^\[\^\d+\]:.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[\^\d+\]", "", text)  # e.g., "[^0]"

    # Emphasis/strong
    # **bold** -> bold ; *italics* -> italics ; _em_ -> em
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.replace("*", "")

    # Horizontal rules (three or more -, *, _ in a line)
    text = re.sub(r"(?m)^\s*([-*_]\s*){3,}\s*$", "", text)
    return text.strip()

def clean_text_for_output(text: str) -> str:
    """
    Full cleaning:
    - remove Markdown/HTML (preserving anchor text)
    - normalize Unicode->ASCII
    - compact line breaks
    Args:
        text (str): Input text to clean.
    Returns:
        str: Cleaned text.
    """
    text = remove_markdown_headers(text)
    text = normalize_unicode_to_ascii(text)

    # Compact multiple line breaks
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Trim spaces
    return text.strip()


#--- Chunking functions ---
def split_by_structure(text: str, max_tokens: int, overlap_frac: float) -> List[str]:
    """
    Split while respecting basic structure:
    1) Splits by H1-H3 headers (keeping the titles inside the chunk).
    2) Within each section, uses sentence packing to approximate max_tokens.
    Args:
        text (str): Input text to split.
        max_tokens (int): Maximum tokens per chunk.
        overlap_frac (float): Fraction of overlap between chunks (0.0 to 0.5).
    Returns:
        List[str]: List of text chunks.
    """
    assert 0.0 <= overlap_frac <= 0.5, "overlap_frac must be between 0.0 and 0.5"
    sections = []
    last_pos = 0
    for m in HEADER_SPLIT_RE.finditer(text):
        start = m.start()
        if start > last_pos:
            sections.append(text[last_pos:start])
        last_pos = start
    # Last section
    sections.append(text[last_pos:])

    # Simple sentence splitter
    sentence_re = re.compile(SENTENCE_SPLIT_RE, re.DOTALL)

    chunks: List[str] = []
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        # Split into "sentences"
        sents = []
        for sm in sentence_re.finditer(sec):
            sents.append(sm.group(0))
        # If no sentences detected, treat the whole block
        if not sents:
            sents = [sec]

        # Greedy packing up to max_tokens
        buffer = []
        buffer_tok = 0
        for s in sents:
            stoks = count_tokens(s)
            if buffer and (buffer_tok + stoks) > max_tokens:
                chunks.append("".join(buffer).strip())
                if overlap_frac > 0 and len(buffer) > 1:
                    overlap_count = max(1, int(len(buffer) * overlap_frac))
                    seed = buffer[-overlap_count:]
                    buffer = seed + [s]
                    buffer_tok = sum(count_tokens(x) for x in buffer)
                else:
                    buffer = [s]
                    buffer_tok = stoks
            else:
                buffer.append(s)
                buffer_tok += stoks
        if buffer:
            candidate = "".join(buffer).strip()
            # Evitar guardar si es demasiado corto o igual al solapamiento
            if not chunks or len(candidate) > len(chunks[-1]) * overlap_frac:
                chunks.append(candidate)

    return [c for c in chunks if c]


def is_low_value_chunk(text: str) -> bool:
    """
    Heuristic to detect low-information-value chunks.

    Args:
        text (str): Input text chunk to evaluate.
    Returns:
        bool: True if the chunk is considered low-value, False otherwise.
    """
    if count_tokens(text) < 50:
        return True
    low = text.lower()
    for pat in LOW_VALUE_PATTERNS:
        if re.search(pat, low):
            return True
    return False

def split_by_chars_estimate(chunk: str, max_tokens: int) -> list[str]:
    """
    Splits a very long chunk by characters instead of by words/tokens.
    Estimates ~4 characters per token and tries to cut at double newlines (\n\n).
    Args:
        chunk (str): Input text chunk to split.
        max_tokens (int): Maximum tokens per resulting chunk.
    Returns:
        List[str]: List of text chunks.
    
    """
    if not chunk:
        return []
    target_chars = max(1, int(max_tokens * 4))  # 4 chars ~ 1 token
    parts = []
    i = 0
    n = len(chunk)

    while i < n:
        j = min(n, i + target_chars) # initial cut
        # try to expand up to the next double paragraph break if nearby
        k = j
        for off in range(200):  # small margin
            if j + off < n and chunk[j + off:j + off + 2] == "\n\n":
                k = j + off
                break
        parts.append(chunk[i:k].strip())
        i = k if k > i else j

    # clean up any residual empties
    return [p for p in parts if p]

def split_chunk_by_sentences(chunk: str, max_tokens: int) -> list[str]:
    """
    Splits a chunk by sentence boundaries until max_tokens is satisfied.
    If no sentences are detected, falls back to _split_by_chars_estimate.
    Args:
        chunk (str): Input text chunk to split.
        max_tokens (int): Maximum tokens per resulting chunk.
    Returns:
        List[str]: List of text chunks.
    """
    sentence_re = re.compile(SENTENCE_SPLIT_RE, re.DOTALL)
    sents = [m.group(0) for m in sentence_re.finditer(chunk)]
    if not sents:
        # Efficient fallback: split by characters (fast and safe)
        return split_by_chars_estimate(chunk, max_tokens)

    parts = []
    buf, btok = [], 0
    for s in sents:
        st = count_tokens(s)
        if buf and btok + st > max_tokens:
            parts.append("".join(buf))
            buf, btok = [s], st
        else:
            buf.append(s)
            btok += st
    if buf:
        parts.append("".join(buf))

    return [p for p in parts if p and p.strip()]


def postprocess_merge_and_split(chunks: list[str], min_tokens: int, max_tokens: int) -> list[str]:
    """
    Double pass:
      1) Forward: 
         - 'strict' merge if chunk < min/2 (if it doesn't fit, tries to split the next so it fits),
         - merge if < min_tokens or is low-value (usual rule).
      2) Backward: avoid a small leftover chunk at the end if possible.
      3) Final splits:
         - hard limit: if > 2*max_tokens -> split by characters and then refine by sentences,
         - if max_tokens < size <= 2*max_tokens -> split by sentences.
    Args:
        chunks (List[str]): List of initial text chunks.
        min_tokens (int): Minimum tokens per chunk.
        max_tokens (int): Maximum tokens per chunk.
    Returns:
        List[str]: List of processed text chunks.
    """
    if not chunks:
        return []

    strict_min = max(1, int(min_tokens / 2))
    merged: list[str] = []
    i = 0

    while i < len(chunks):
        cur = (chunks[i] or "").strip()
        if not cur:
            i += 1
            continue

        cur_tok = count_tokens(cur)
        cur_low = is_low_value_chunk(cur)

        # ---- Strict merge: everything below min/2 is always merged ----
        if cur_tok < strict_min and i + 1 < len(chunks):
            nxt = (chunks[i + 1] or "").strip()
            if nxt:
                combined = cur_tok + count_tokens(nxt)
                if combined > max_tokens:
                    # Try to split the next so the merge fits
                    room = max(1, max_tokens - cur_tok)
                    split_nxt = split_chunk_by_sentences(nxt, room) or split_by_chars_estimate(nxt, room)
                    if split_nxt:
                        new_cur = (cur + "\n\n" + split_nxt[0]).strip()
                        merged.append(new_cur)
                        # Re-inject the rest of nxt's parts into the original sequence
                        chunks = chunks[:i + 1] + split_nxt[1:] + chunks[i + 2:]
                        i += 1
                        continue
                    # If it still doesn't fit, fall through to normal flow (below)
                else:
                    # It fits, merge directly
                    merged.append((cur + "\n\n" + nxt).strip())
                    i += 2
                    continue

        # ---- Usual rule: merge if < min_tokens or is low-value ----
        if (cur_tok < min_tokens or cur_low) and (i + 1 < len(chunks)):
            nxt = (chunks[i + 1] or "").strip()
            if nxt and (cur_tok + count_tokens(nxt)) <= max_tokens:
                merged.append((cur + "\n\n" + nxt).strip())
                i += 2
                continue

        # If not merged, emit current
        merged.append(cur)
        i += 1

    # ---- Backward: avoid a small last chunk if it can be merged with the previous ----
    if len(merged) >= 2 and count_tokens(merged[-1]) < min_tokens:
        if (count_tokens(merged[-1]) + count_tokens(merged[-2])) <= max_tokens:
            merged[-2] = (merged[-2] + "\n\n" + merged[-1]).strip()
            merged.pop()

    # ---- Hard limit splits ----
    final_chunks: list[str] = []
    hard_limit = 2 * max_tokens

    for c in merged:
        tok = count_tokens(c)
        if tok > hard_limit:
            # 1) split by characters (robust for text without punctuation)
            parts = split_by_chars_estimate(c, max_tokens)
            # 2) refine by sentences if any part still exceeds max
            for p in parts:
                if count_tokens(p) > max_tokens:
                    final_chunks.extend(split_chunk_by_sentences(p, max_tokens))
                else:
                    final_chunks.append(p)
        elif tok > max_tokens:
            # normal case: exceeds max but not the hard limit
            final_chunks.extend(split_chunk_by_sentences(c, max_tokens))
        else:
            final_chunks.append(c)

    # Clean up any residual empties
    final_chunks = [c for c in final_chunks if c and c.strip()]

    try:
        over = sum(1 for c in final_chunks if count_tokens(c) > max_tokens)
        under = sum(1 for c in final_chunks if count_tokens(c) < min_tokens)
        logger.info(f"Postprocess: {len(final_chunks)} chunks "
                    f"(under<{min_tokens}: {under}, over>{max_tokens}: {over})")
    except Exception:
        pass

    return final_chunks

def enforce_limits_after_cleaning(chunks: list[str]) -> list[str]:
    """
    Re-applies limits after cleaning: splits any chunk > CHUNK_MAX_TOKENS.
    Uses sentence splitting first, and if not possible, splits by characters.
    Args:
        chunks (List[str]): List of text chunks to process.
    Returns:
        List[str]: List of text chunks within the token limits.
    """
    out: list[str] = []
    for ch in chunks:
        tok = count_tokens(ch)
        if tok > CHUNK_MAX_TOKENS:
            parts = split_chunk_by_sentences(ch, CHUNK_MAX_TOKENS)
            if not parts:
                parts = split_by_chars_estimate(ch, CHUNK_MAX_TOKENS)
            out.extend(parts)
        else:
            out.append(ch)
    return out

def fix_tiny_after_cleaning(chunks: list[str]) -> list[str]:
    """
    Merges ultra-small chunks with the previous one if possible. Avoids tiny residuals (e.g., 1–20 tokens).
    Args:
        chunks (List[str]): List of text chunks to process.
    Returns:
        List[str]: List of text chunks with tiny ones merged.
    """
    out: list[str] = []
    hard_min = 20  # absolute minimum to avoid tiny chunks  
    for ch in chunks:
        tok = count_tokens(ch)
        if tok >= hard_min or not out:
            out.append(ch)
        else:
            # Try to merge with the previous chunk if it fits within the limit
            if count_tokens(out[-1]) + tok <= CHUNK_MAX_TOKENS:
                out[-1] = (out[-1] + "\n\n" + ch).strip()
    return out


#--- Functions to build and save final JSON objects ---
def build_chunk_objects(chunks: List[str], formulas_map: Dict[str, str], code_map: Dict[str, str], tables_map: Dict[str, str]) -> List[Dict]:
    """
    Builds 'chunk' objects with page_content and metadata.
    Note: keeps placeholders [FORMULA_i] / [CODE_k] / [TABLE_j] in page_content.

    Args:
        chunks (List[str]): List of text chunks.
        formulas_map (Dict[str, str]): Map of formula placeholders to original LaTeX.
        code_map (Dict[str, str]): Map of code placeholders to original code.
        tables_map (Dict[str, str]): Map of table placeholders to original tables.
    Returns:
        List[Dict]: List of chunk objects with metadata.
    """
    out = []
    for i, ch in enumerate(chunks, start=1):
        tok = count_tokens(ch)
        # Determine if the chunk contains any FORMULA_i / CODE_k
        contains_formula = bool(re.search(r"\[FORMULA_\d+\]", ch))
        contains_code = bool(re.search(r"\[CODE_\d+\]", ch))
        contains_table = bool(re.search(r"\[TABLE_\d+\]", ch))
        # Filter maps to the keys that actually appear in this chunk
        t_subset = {k: v for k, v in tables_map.items() if k in ch}
        f_subset = {k: v for k, v in formulas_map.items() if k in ch or any(k in table_text for table_text in t_subset.values())} # formulas may appear inside tables
        c_subset = {k: v for k, v in code_map.items() if k in ch}
        

        meta = {
            "token_count": tok,
            "contains_formula": contains_formula,
            "formulas": f_subset,
            "contains_code": contains_code,
            "code": c_subset,
            "contains_table": contains_table,
            "tables": t_subset,
        }
        out.append(
            {
                "chunk_id": i,
                "page_content": ch,
                "metadata": meta,
            }
        )
    return out

def build_paper_object(md_path: Path, chunk_objs: List[Dict]) -> Dict:
    """
    Builds the final 'paper' object with aggregated statistics.
    Args:
        md_path (Path): Path to the original Markdown file.
        chunk_objs (List[Dict]): List of chunk objects.
    Returns:
        Dict: The final paper object.
    """
    token_sizes = [c["metadata"]["token_count"] for c in chunk_objs] or [0]
    return {
        "version": "1.0",
        "mode": "improved",
        "paper": {
            "paper_id": md_path.stem,
            "source_file": md_path.name,
            "num_chunks": len(chunk_objs),
            "min_chunk_size": min(token_sizes),
            "max_chunk_size": max(token_sizes),
        },
        "chunks": chunk_objs,
    }

def save_json_per_paper(paper_obj: Dict, output_dir: str, md_path: Path) -> None:
    """
    Guarda el JSON con el mismo nombre del .md, pero extensión .json.
    """
    os.makedirs(output_dir, exist_ok=True)
    out_path = Path(output_dir) / (md_path.stem + ".json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(paper_obj, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved: {out_path}")

#--- Main processing pipeline per file ---
def read_markdown(md_path: Path) -> str:
    """ Reads the content of a Markdown file.
    Args:
        md_path (Path): Path to the Markdown file.
    Returns:
        str: Content of the Markdown file.
    """
    with open(md_path, "r", encoding="utf-8") as f:
        return f.read()

def clean_and_prepare_text(raw_text: str) -> Tuple[str, Dict[str, str], Dict[str, str], Dict[str, str]]:
    """
    Preprocessing pipeline:
    - Extract code -> placeholders
    - Protect formulas -> placeholders
    - Extract tables -> placeholders
    - Remove images ![...](...)
    Returns: prepared_text, formulas_map, code_map , tables_map
    (The full cleaning occurs later, per chunk.)

    Args:
        raw_text (str): Raw input text to preprocess.
    Returns:
        Tuple[str, Dict[str, str], Dict[str, str], Dict[str, str]]: Prepared text, formulas map, code map, tables map.
    """
    t1, code = extract_and_placeholder_code(raw_text)
    logger.debug(f"Extracted {len(code)} code blocks")
    t2, formulas = extract_and_protect_formulas(t1)
    logger.debug(f"Extracted {len(formulas)} formulas")
    t3, tables = extract_and_protect_tables(t2)
    logger.debug(f"Extracted {len(tables)} tables")
    t4 = remove_markdown_images(t3)
    logger.debug("Removed Markdown images")
    t5 = preclean_for_chunking(t4)
    logger.debug("Pre-cleaned text for chunking")
    return t5, formulas, code, tables

def process_single_file(md_path: Path, index: int, total: int) -> Tuple[bool, Dict]:
    """
    Processes a .md file to JSON (improved chunking) and saves output.
    Returns (ok, stats) for summary.

    Args:
        md_path (Path): Path to the Markdown file.
        index (int): Index of the file in the processing sequence.
        total (int): Total number of files to process.
    Returns:
        Tuple[bool, Dict]: (Success flag, statistics dictionary).
    """
    try:
        logger.info(f"[{index+1}/{total}] Processing: {md_path}")
        t0 = time.perf_counter()

        raw = read_markdown(md_path)
        logger.info(f"{md_path.name} - read OK ({len(raw)} chars)")

        if not raw.strip():
            logger.warning(f"Empty file skipped: {md_path}")
            return False, {}

        # Initial preparation
        prepared_text, formulas_map, code_map, tables_map = clean_and_prepare_text(raw)
        logger.info(f"{md_path.name} - placeholders OK "
                    f"(formulas={len(formulas_map)}, code={len(code_map)}, tables={len(tables_map)})")

        # Structural split + post-processing
        initial_chunks = split_by_structure(
            prepared_text, max_tokens=CHUNK_MAX_TOKENS, overlap_frac=CHUNK_OVERLAP_FRAC
        )
        logger.info(f"{md_path.name} - split_by_structure -> {len(initial_chunks)} chunks")

        processed_chunks = postprocess_merge_and_split(
            initial_chunks, min_tokens=CHUNK_MIN_TOKENS, max_tokens=CHUNK_MAX_TOKENS
        )
        logger.info(f"{md_path.name} - postprocess -> {len(processed_chunks)} chunks")

        # Final cleaning + token recount, output construction
        before = len(processed_chunks)
        cleaned_chunks: List[str] = [clean_text_for_output(ch) for ch in processed_chunks]
        logger.info(f"{md_path.name} - cleaning done")
        
        # Re-enforce limits after cleaning (some chunks may have grown)
        cleaned_chunks = enforce_limits_after_cleaning(cleaned_chunks)
        # Ensure no tiny chunks remain
        cleaned_chunks = fix_tiny_after_cleaning(cleaned_chunks)
        logger.info(f"{md_path.name} - post-clean enforce: {before} -> {len(cleaned_chunks)} chunks")
    

        chunk_objs = build_chunk_objects(cleaned_chunks, formulas_map, code_map, tables_map)
        paper_obj = build_paper_object(md_path, chunk_objs)

        # Save (same .md name -> .json) in improved folder
        save_json_per_paper(paper_obj, CHUNKING_IMPROVED_OUTPUT_DIR, md_path)
        elapsed = time.perf_counter() - t0
        logger.info(f"{md_path.name} - done in {elapsed:.2f}s")

        # Stats for summary
        sizes = [c["metadata"]["token_count"] for c in chunk_objs]
        stats = {
            "paper": md_path.name,
            "chunks": len(chunk_objs),
            "min": min(sizes) if sizes else 0,
            "max": max(sizes) if sizes else 0,
            "avg": (sum(sizes) / len(sizes)) if sizes else 0.0,
            "in_range_pct": (
                100.0
                * sum(1 for s in sizes if CHUNK_MIN_TOKENS <= s <= CHUNK_MAX_TOKENS)
                / len(sizes)
            ) if sizes else 0.0,
        }
        return True, stats

    except Exception as e:
        logger.error(f"Error processing {md_path}: {e}")
        traceback.print_exc()
        return False, {}

def final_summary(stats_list: List[Dict]) -> None:
    """
    Emits a final summary block with aggregated metrics.

    Args:
        stats_list (List[Dict]): List of statistics dictionaries from processed files.
    """
    total_papers = len([s for s in stats_list if s])
    total_chunks = sum(s.get("chunks", 0) for s in stats_list if s)

    # Calculate % in range globally
    # (without individual sizes, we approximate by weighting 'in_range_pct' by 'chunks')
    in_range_weighted = 0.0
    for s in stats_list:
        if not s or s.get("chunks", 0) == 0:
            continue
        in_range_weighted += s["in_range_pct"] * s["chunks"]
    in_range_global_pct = (in_range_weighted / total_chunks) if total_chunks else 0.0

    # For global min/max/avg, we approximate with the weighted mean of means by chunks
    avg_weighted = 0.0
    min_vals = [s["min"] for s in stats_list if s]
    max_vals = [s["max"] for s in stats_list if s]
    for s in stats_list:
        if not s or s.get("chunks", 0) == 0:
            continue
        avg_weighted += s["avg"] * s["chunks"]
    avg_global = (avg_weighted / total_chunks) if total_chunks else 0.0

    logger.info("========== FINAL SUMMARY (IMPROVED CHUNKING) ==========")
    logger.info(f"Papers processed: {total_papers}")
    logger.info(f"Total chunks:     {total_chunks}")
    if min_vals:
        logger.info(f"Min size (per-paper min): {min(min_vals)}")
    if max_vals:
        logger.info(f"Max size (per-paper max): {max(max_vals)}")
    logger.info(f"Avg size (weighted): {avg_global:.2f}")
    logger.info(f"Compliance [{CHUNK_MIN_TOKENS}..{CHUNK_MAX_TOKENS}] : {in_range_global_pct:.2f}%")
    logger.info("=======================================================")

def main():
    try:       
        if not os.path.exists(CHUNKING_IMPROVED_OUTPUT_DIR):
            os.makedirs(CHUNKING_IMPROVED_OUTPUT_DIR, exist_ok=True)
            logger.info(f"Created directory: {CHUNKING_IMPROVED_OUTPUT_DIR}")

        if not os.path.exists(CLEANED_DATA_PATH_MD):
            logger.error(f"Input directory does not exist: {CLEANED_DATA_PATH_MD}")
            return
        md_files = list(iter_markdown_files(CLEANED_DATA_PATH_MD))
        total = len(md_files)
        logger.info(f"Found {total} markdown files in: {CLEANED_DATA_PATH_MD}")

        stats_list: List[Dict] = []
        for idx, md_path in enumerate(sorted(md_files)):
            ok, stats = process_single_file(md_path, idx, total)
            if ok:
                stats_list.append(stats)

        final_summary(stats_list)
    except Exception as e:
        logger.error(f"Fatal error in main: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
