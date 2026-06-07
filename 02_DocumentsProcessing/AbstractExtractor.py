import re
from typing import Optional, Tuple, List
from LoggerSetUp import setup_logger
import os


from config import(
    RAW_DATA_PATH_MD_MISTRAL,
    NOT_FOUND_ABSTRACT_FILE,
    ABSTRACTS_PATH,
    LOGS_BASE_PATH,
    LOG_LEVEL
)

# Configure logger
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='AbstractExtractor.log',
    error_log_filename='AbstractExtractor_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)


# --------- Regex helpers (OCR tolerant) ---------
def spaced_word_regex(word: str) -> str:
    """
    Build a regex pattern that matches a word even if OCR inserted spaces,
    dots, dashes, or underscores between letters.

    Args:
        word (str): The target word (e.g., "abstract").

    Returns:
        str: Regex pattern string that matches OCR-noisy variants of the word.
    """
    chars = list(word)
    between = r"[\s\.\-_/]*"
    return "".join(re.escape(c) + between for c in chars[:-1]) + re.escape(chars[-1])


def heading_pattern_for(keyword: str) -> re.Pattern:
    """
    Build a regex pattern to match Markdown headings like '# Abstract',
    tolerating numbers between the '#' and the word, and OCR spacing.

    Args:
        keyword (str): The keyword to detect (e.g., "abstract").

    Returns:
        re.Pattern: Compiled regex pattern.
    """
    kw = spaced_word_regex(keyword)
    pat = rf"(?im)^[ \t]{{0,3}}#{{1,6}}[ \t]+(?:\d+[ \t]+)?{kw}\b[ \t\.:]*$"
    return re.compile(pat)


def label_line_pattern_for(keyword: str, punct=r"[:\.-—]") -> re.Pattern:
    """
    Build a regex pattern to match lines like 'Abstract:' or 'Abstract.',
    tolerating OCR spacing.

    Args:
        keyword (str): The keyword to detect (e.g., "abstract").
        punct (str): Regex for allowed punctuation after the keyword.

    Returns:
        re.Pattern: Compiled regex pattern.
    """
    kw = spaced_word_regex(keyword)
    pat = rf"(?im)^[ \t]*\**[ \t]*{kw}[ \t]*\**[ \t]*{punct}"
    return re.compile(pat)

def extract_background_block(lines: List[str], start_idx: int,
                             stop_patterns: List[re.Pattern],
                             max_paragraphs: int = 3) -> Optional[str]:
    """
    Extract a block starting with 'Background:' and ending strictly with a
    paragraph that begins with 'Conclusion:' or 'Results:'.
    If either boundary is missing, return None.

    Args:
        lines (List[str]): Document lines.
        start_idx (int): Index of the 'Background:' line.
        stop_patterns (List[re.Pattern]): Patterns for valid end markers.
        max_paragraphs (int): Maximum paragraphs to include (default=3).

    Returns:
        Optional[str]: Extracted text or None if conditions not met.
    """
    # Determine the start paragraph
    s, e = paragraph_bounds_around(lines, start_idx)

    paragraphs = [(s, e)]
    cursor = e

    while len(paragraphs) < max_paragraphs:
        # skip blanks
        while cursor < len(lines) and lines[cursor].strip() == "":
            cursor += 1
        if cursor >= len(lines):
            break

        ns, ne = paragraph_bounds_around(lines, cursor)
        paragraphs.append((ns, ne))
        cursor = ne

        # stop if we've just included a paragraph starting with Conclusion/Results
        if any(pat.match(lines[ns] or "") for pat in stop_patterns):
            break

    # check last paragraph is a valid stop
    if not any(pat.match(lines[paragraphs[-1][0]] or "") for pat in stop_patterns):
        return None

    start = paragraphs[0][0]
    end = paragraphs[-1][1]
    return slice_text(lines, start, end)



# --------- Line utilities ---------
def next_heading_index(lines: List[str], start_idx: int) -> int:
    """
    Find the index of the next Markdown heading starting after a given line.

    Args:
        lines (List[str]): Document lines.
        start_idx (int): Current line index.

    Returns:
        int: Index of the next heading, or len(lines) if none found.
    """
    pat = re.compile(r"(?im)^[ \t]{0,3}#{1,6}[ \t]+\S")
    for i in range(start_idx + 1, len(lines)):
        if pat.match(lines[i]):
            return i
    return len(lines)


def slice_text(lines: List[str], i: int, j: int) -> str:
    """
    Extract and clean a slice of text between two line indices.

    Args:
        lines (List[str]): Document lines.
        i (int): Start index (inclusive).
        j (int): End index (exclusive).

    Returns:
        str: Joined text between lines[i:j], stripped.
    """
    return "\n".join(lines[i:j]).strip()


def paragraph_bounds_around(lines: List[str], idx: int) -> Tuple[int, int]:
    """
    Find the boundaries of the paragraph containing a given line.

    A paragraph is defined as a sequence of non-empty lines separated by one
    or more blank lines.

    Args:
        lines (List[str]): Document lines.
        idx (int): Index of the line inside the paragraph.

    Returns:
        Tuple[int, int]: (start_index, end_index_exclusive) of the paragraph.
    """
    s = idx
    while s - 1 >= 0 and lines[s - 1].strip() != "":
        s -= 1
    e = idx
    while e + 1 < len(lines) and lines[e + 1].strip() != "":
        e += 1
    return s, e + 1


def collect_until_stop(lines: List[str], start_line: int, stop_tests: List[re.Pattern]) -> str:
    """
    Collect lines starting from a given index until:
      - another Markdown heading is found, or
      - any stop regex pattern matches, or
      - the end of the file is reached.

    Args:
        lines (List[str]): Document lines.
        start_line (int): Index to start collecting from.
        stop_tests (List[re.Pattern]): Regex patterns that indicate stopping.

    Returns:
        str: Extracted text block.
    """
    end = len(lines)
    end = min(end, next_heading_index(lines, start_line))
    for i in range(start_line, end):
        for pat in stop_tests:
            if pat.search(lines[i]):
                end = min(end, i)
                break
    return slice_text(lines, start_line, end)


def non_empty(s: str) -> bool:
    """
    Check if a string is non-empty after stripping whitespace.

    Args:
        s (str): Input string.

    Returns:
        bool: True if non-empty, False otherwise.
    """
    return s is not None and s.strip() != ""

def is_indented(paragraph: str) -> bool:
        """
        Return True if the first non-empty line starts with spaces/tabs (i.e., visually shifted to the right).
        """
        for line in paragraph.splitlines():
            if line.strip() == "":
                continue
            # If line starts with space or tab before any non-space, it's indented
            return bool(re.match(r"^[ \t]+", line))
        return False  # empty paragraph is not considered indented


def collect_n_paragraphs_until(
    lines: List[str],
    start_idx: int,
    max_paragraphs: int,
    stop_tests: List[re.Pattern],
    stop_on_heading: bool = True,
) -> str:
    """
    Collect up to `max_paragraphs` contiguous paragraphs starting from the paragraph
    that contains `start_idx`. Stop earlier if a stop pattern or (optionally) a Markdown
    heading is encountered.

    This is tailored for the "Background: ... [N paragraphs max 3] ... Conclusion:/Results:"
    scenario (case 6).

    Args:
        lines (List[str]): Document lines.
        start_idx (int): Index within the first paragraph to include.
        max_paragraphs (int): Maximum number of paragraphs to collect.
        stop_tests (List[re.Pattern]): Regexes that indicate a hard stop (e.g., 'Conclusion:', 'Results:').
        stop_on_heading (bool): If True, stop when a Markdown heading is encountered.

    Returns:
        str: The collected text block (without including the stop line).
    """
    assert max_paragraphs >= 1, "max_paragraphs must be >= 1"

    # Optional heading detector
    heading_pat = re.compile(r"(?im)^[ \t]{0,3}#{1,6}[ \t]+\S")

    # Start with the paragraph that contains start_idx
    s, e = paragraph_bounds_around(lines, start_idx)

    # If a stop condition appears inside the starting paragraph, cut there
    for i in range(s, e):
        if (stop_on_heading and heading_pat.match(lines[i] or "")) or any(
            pat.match(lines[i] or "") for pat in stop_tests
        ):
            return slice_text(lines, s, i)

    para_count = 1
    end_cursor = e

    while para_count < max_paragraphs:
        # Find the next paragraph start
        i = end_cursor
        # Skip blank lines
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        if i >= len(lines):
            break

        # If next line is a heading or stop pattern, do not include it; stop here
        if stop_on_heading and heading_pat.match(lines[i] or ""):
            break
        if any(pat.match(lines[i] or "") for pat in stop_tests):
            break

        # Determine next paragraph bounds
        ns, ne = paragraph_bounds_around(lines, i)

        # Scan inside the upcoming paragraph for stop/heading; if found, cut before it
        cut_at = None
        for j in range(ns, ne):
            if (stop_on_heading and heading_pat.match(lines[j] or "")) or any(
                pat.match(lines[j] or "") for pat in stop_tests
            ):
                cut_at = j
                break

        if cut_at is not None:
            end_cursor = min(cut_at, ne)
            break

        # Include the full paragraph
        end_cursor = ne
        para_count += 1

    return slice_text(lines, s, end_cursor)


# --------- Main function ---------
def extract_abstract(md_text: str) -> Optional[str]:
    """
    Extract the abstract from OCR-processed Markdown text, following a strict
    hierarchy of rules:

      1. Heading '# ... Abstract' (last non-empty if multiple).
      2. Heading '# ... Synopsis' (last non-empty if multiple).
      3. Heading '# ... Summary' (last non-empty if multiple).
      4. A line starting with 'Abstract:' or 'Abstract.'.
      5. The paragraph immediately before '# ... Keywords'.
      6. A block starting with 'Background:' and including up to 3 paragraphs,
         but cutting earlier if 'Conclusion:' or 'Results:' (or a new heading) appears.
      7. If none of the above, take the paragraph before the first 'Keywords:' or 'Key words:'.
      7.B. If still none, take the paragraph before the first 'CCS Concepts:'.

    Args:
        md_text (str): Full Markdown document text.

    Returns:
        Optional[str]: Extracted abstract, or None if nothing matches.
    """
    lines = md_text.splitlines()

    # Keyword patterns
    h_abs = heading_pattern_for("abstract")
    h_syn = heading_pattern_for("synopsis")
    h_sum = heading_pattern_for("summary")
    h_keyw = heading_pattern_for("keywords")
    h_ccs = heading_pattern_for("ccs[ \t]*concepts")
    h_intro = heading_pattern_for("introduction")

    l_abs_colon = label_line_pattern_for("abstract")
    l_bg = label_line_pattern_for("background")
    l_conc = label_line_pattern_for("conclusion")
    l_res = label_line_pattern_for("results")
    l_keywords_anywhere = re.compile(
        rf"(?im)^[ \t]*{spaced_word_regex('key')}{r'[ \t]*'}{spaced_word_regex('words')}[ \t]*[:\.]|^[ \t]*{spaced_word_regex('keywords')}[ \t]*[:\.-]?"
    )
    l_ccs_anywhere = re.compile(r"(?im)^[ \t]*CCS[ \t]*Concepts[ \t]*[:\.-]")

    # --- 1: '# ... Abstract' ---
    abs_idxs = [i for i, ln in enumerate(lines) if h_abs.match(ln or "")]
    if abs_idxs:

        for idx in reversed(abs_idxs):
            start = idx + 1
            end = next_heading_index(lines, idx)
            sec = slice_text(lines, start, end)
            if non_empty(sec):
                return sec
            
        start = abs_idxs[-1] + 1
        end = next_heading_index(lines, abs_idxs[-1])
        fallback = slice_text(lines, start, end)
        if non_empty(fallback):
            return fallback

    # --- 2: '# ... Synopsis' ---
    syn_idxs = [i for i, ln in enumerate(lines) if h_syn.match(ln or "")]
    if syn_idxs:
        for idx in reversed(syn_idxs):
            sec = slice_text(lines, idx + 1, next_heading_index(lines, idx))
            if non_empty(sec):
                return sec
        return slice_text(lines, syn_idxs[-1] + 1, next_heading_index(lines, syn_idxs[-1]))

    # --- 3: '# ... Summary' ---
    sum_idxs = [i for i, ln in enumerate(lines) if h_sum.match(ln or "")]
    if sum_idxs:
        for idx in reversed(sum_idxs):
            sec = slice_text(lines, idx + 1, next_heading_index(lines, idx))
            if non_empty(sec):
                return sec
        return slice_text(lines, sum_idxs[-1] + 1, next_heading_index(lines, sum_idxs[-1]))

    # --- 4: 'Abstract:' / 'Abstract.' ---
    lab_abs_idxs = [i for i, ln in enumerate(lines) if l_abs_colon.match(ln or "")]
    if lab_abs_idxs:
        start = lab_abs_idxs[-1]
        return collect_until_stop(lines, start, [l_keywords_anywhere, l_ccs_anywhere])

    # --- 5: paragraph before '# ... Keywords' ---
    keyw_head_idxs = [i for i, ln in enumerate(lines) if h_keyw.match(ln or "")]
    if keyw_head_idxs:
        kw_idx = keyw_head_idxs[0]
        prev_nonblank = kw_idx - 1
        while prev_nonblank >= 0 and lines[prev_nonblank].strip() == "":
            prev_nonblank -= 1
        if prev_nonblank >= 0:
            s, e = paragraph_bounds_around(lines, prev_nonblank)
            return slice_text(lines, s, e)

    # --- 6: 'Background:' ... must end at 'Conclusion:' or 'Results:' ---
    bg_idxs = [i for i, ln in enumerate(lines) if l_bg.match(ln or "")]
    if bg_idxs:
        start = bg_idxs[0]
        abstract = extract_background_block(
            lines=lines,
            start_idx=start,
            stop_patterns=[l_conc, l_res],
            max_paragraphs=3
        )
        if non_empty(abstract):
            return abstract


    # --- 7: no explicit start, end at first 'Keywords:' ---
    kw_any_idxs = [i for i, ln in enumerate(lines) if l_keywords_anywhere.match(ln or "")]
    if kw_any_idxs:
        kw = kw_any_idxs[0]
        end_idx = kw - 1
        while end_idx >= 0 and lines[end_idx].strip() == "":
            end_idx -= 1
        if end_idx >= 0:
            s_up, e_up = paragraph_bounds_around(lines, end_idx)
            return slice_text(lines, s_up, e_up)

    # --- 7.B: no explicit start, end at first 'CCS Concepts' ---
    ccs_any_idxs = [i for i, ln in enumerate(lines) if l_ccs_anywhere.match(ln or "")]
    if ccs_any_idxs:
        ccs = ccs_any_idxs[0]
        end_idx = ccs - 1
        while end_idx >= 0 and lines[end_idx].strip() == "":
            end_idx -= 1
        if end_idx >= 0:
            s_up, e_up = paragraph_bounds_around(lines, end_idx)
            return slice_text(lines, s_up, e_up)
        
    h_intro = heading_pattern_for("introduction")

    # --- 8: '# ... Abstract' followed by up to 5 section headings, then '# ... Introduction' ---
    # Re-find Abstract headings (OCR/spacing tolerant)
    abs_idxs_c8 = [i for i, ln in enumerate(lines) if h_abs.match(ln or "")]
    if abs_idxs_c8:
        # Try each Abstract heading in order; pick the first that satisfies the structure.
        for abs_idx in abs_idxs_c8:
            sections = []    # indices of intermediate section headings between Abstract and Introduction
            cursor = abs_idx
            # Collect up to 5 headings after Abstract **until** we hit Introduction
            for _ in range(6):  # allow scanning up to 6 next headings (5 sections + 1 intro)
                nxt = next_heading_index(lines, cursor)
                if nxt >= len(lines):
                    break  # no next heading: pattern not satisfied
                # If the next heading is 'Introduction', stop scanning here
                if h_intro.match(lines[nxt] or ""):
                    break
                # Otherwise, it's one intermediate section
                sections.append(nxt)
                cursor = nxt

            # The heading immediately after the last collected section must be 'Introduction'
            nxt_after = next_heading_index(lines, cursor)
            if (
                1 <= len(sections) <= 5
                and nxt_after < len(lines)
                and h_intro.match(lines[nxt_after] or "")
            ):
                # Concatenate the content of each collected section (title excluded)
                parts = []
                for hidx in sections:
                    start = hidx + 1
                    end = next_heading_index(lines, hidx)
                    chunk = slice_text(lines, start, end)
                    if non_empty(chunk):
                        parts.append(chunk)
                if parts:
                    return "\n\n\n".join(parts).strip()

    return None

def clean_abstract(abstract: str) -> str:
    """
    Clean an extracted abstract with OCR quirks by removing:
      1) Any standalone footnote marker line like "[^N]".
         Additionally, remove the *immediately following paragraph* (whether or not
         there's a blank line), and then
      2) Any footnote-definition paragraph starting with "[^N]:".
      3) After (1) and/or (2), remove all *subsequent* paragraphs that are indented
         (start with spaces/tabs) until a non-indented paragraph is encountered.
      4) Any paragraph that starts with an email bullet like "* E-mail:" (variant-tolerant).

    IMPORTANT:
      - Paragraphs are segmented *logically*: a new paragraph starts at a blank line,
        a line that is exactly "[^N]", or a line that starts with "[^N]:", even if
        there is no blank line separating them in the source.
      - Indentation means the first non-empty line of the paragraph starts with spaces or tabs.

    Args:
        abstract (str): The markdown/plaintext block containing the abstract.

    Returns:
        str: The cleaned abstract with kept paragraphs re-joined by a blank line.
    """
    lines = abstract.splitlines()

    marker_line_pat = re.compile(r"^\s*\[\^\d+\]\s*$")            # e.g., "[^0]"
    footnote_def_pat = re.compile(r"^\s*\[\^\d+\]\s*:\s*", re.IGNORECASE)  # e.g., "[^0]: ..."
    email_bullet_pat = re.compile(
        r"""^\s*                 # leading spaces
            (?:[\*\-•]\s*)?      # optional bullet
            e[\-\u2010\u2011\u2012\u2013\u2014]?mail\s*:  # E-mail / Email / E-mail
        """,
        re.IGNORECASE | re.VERBOSE
    )

    def is_blank(line: str) -> bool:
        """Return True if the line is blank (whitespace only)."""
        return line.strip() == ""

    def is_indented_paragraph(paragraph: List[str]) -> bool:
        """
        Return True if the first non-empty line of the paragraph starts with spaces/tabs.
        """
        for ln in paragraph:
            if ln.strip() == "":
                continue
            return bool(re.match(r"^[ \t]+", ln))
        return False

    def paragraph_starts_email(paragraph: List[str]) -> bool:
        """
        Return True if the first non-empty line matches the email bullet pattern.
        """
        for ln in paragraph:
            if ln.strip() == "":
                continue
            return bool(email_bullet_pat.match(ln))
        return False

    def next_paragraph(start: int) -> Tuple[Optional[List[str]], int]:
        """
        Build the next logical paragraph starting at index `start`.
        A new paragraph begins when:
          - we encounter a blank line (as usual),
          - OR a line equals "[^N]" (marker) — paragraph is that single line,
          - OR a line starts with "[^N]:" (footnote definition) — paragraph extends
            until the next blank line.
        Returns (paragraph_lines, next_index). If start >= len(lines), returns (None, start).
        """
        n = len(lines)
        i = start
        # skip leading blank lines (they don't form paragraphs on their own)
        while i < n and is_blank(lines[i]):
            i += 1
        if i >= n:
            return None, i

        # Marker line forms a single-line paragraph
        if marker_line_pat.match(lines[i]):
            return [lines[i]], i + 1

        # Footnote definition paragraph: from this line until next blank
        if footnote_def_pat.match(lines[i]):
            para = [lines[i]]
            i += 1
            while i < n and not is_blank(lines[i]) and not marker_line_pat.match(lines[i]) and not footnote_def_pat.match(lines[i]):
                # keep consuming non-blank lines; if another marker/def pops up, we stop
                para.append(lines[i])
                i += 1
            return para, i

        # Normal paragraph: accumulate until a blank OR a marker/definition (which starts a new paragraph)
        para = [lines[i]]
        i += 1
        while i < n:
            if is_blank(lines[i]) or marker_line_pat.match(lines[i]) or footnote_def_pat.match(lines[i]):
                break
            para.append(lines[i])
            i += 1
        return para, i

    # --- Build logical paragraphs ---
    paragraphs: List[List[str]] = []
    idx = 0
    while idx < len(lines):
        para, idx = next_paragraph(idx)
        if para is None:
            break
        paragraphs.append(para)
        # skip any number of blank lines between paragraphs
        while idx < len(lines) and is_blank(lines[idx]):
            idx += 1

    cleaned_paragraphs: List[List[str]] = []
    suppress_next_after_marker = False
    suppress_indented_block = False

    for p in range(len(paragraphs)):
        para = paragraphs[p]

        # Email bullet paragraphs are always dropped
        if paragraph_starts_email(para):
            continue

        # If we just saw a standalone marker, drop the immediate next paragraph and
        # start suppressing indented paragraphs after it.
        if suppress_next_after_marker:
            suppress_next_after_marker = False
            suppress_indented_block = True
            continue

        # Standalone footnote marker "[^N]" — drop it, flag to drop next paragraph
        if len(para) == 1 and marker_line_pat.match(para[0]):
            suppress_next_after_marker = True
            continue

        # Footnote definition "[^N]: ..." — drop it and start suppressing indented paragraphs
        first_line = next((ln for ln in para if ln.strip() != ""), "")
        if footnote_def_pat.match(first_line):
            suppress_indented_block = True
            continue

        # While suppressing, drop paragraphs that are indented; stop when a non-indented appears
        if suppress_indented_block:
            if is_indented_paragraph(para):
                continue
            else:
                suppress_indented_block = False
                # fall through to keep this non-indented paragraph

        cleaned_paragraphs.append(para)

    # Join kept paragraphs with a single blank line between them
    return "\n\n".join("\n".join(p) for p in cleaned_paragraphs).strip()


def extract_single_abstract(input_path: str, output_path: str, index: int, total: int) -> None:
    """
        Extract a single abstract from a document.

        Args:
            input_path (str): The path to the input document.
            output_path (str): The path to the output file for saving the abstract.
            index (int): The index of the current document being processed.
            total (int): The total number of documents to process.
    """

    logger.info(f"[{index+1}/{total}] Extracting abstract from {input_path} to {output_path}")
    # Extract abstract from the input file
    with open(input_path, "r", encoding="utf-8") as infile:
        lines = infile.read()
        abstract = extract_abstract(lines)
        if abstract:
            cln_abstract = clean_abstract(abstract)
            with open(output_path, "w", encoding="utf-8") as outfile:
                outfile.write(cln_abstract)
                logger.info(f"[{index+1}/{total}] Abstract extracted and saved to {output_path}")
        else:
            logger.warning(f" No abstract found in {input_path}")
            with open(NOT_FOUND_ABSTRACT_FILE, "a", encoding="utf-8") as nf:
                nf.write(f"{input_path}\n")

def extract_abstracts(input_path: str, output_path: str):
    """
        Extract abstracts from a collection of documents.

        In this function, we will iterate over all the files in the input directory, 
        extract the abstract from each document, and save it to the output directory.

        Args:
            input_path (str): The path to the input directory containing documents.
            output_path (str): The path to the output directory for saving abstracts.
    """
    logger.info(f"Extracting abstracts from {input_path} to {output_path}")
    # Add your extraction logic here
    total = len(os.listdir(input_path))
    logger.info(f"Total files to process: {total}")
    for index, file_name in enumerate(os.listdir(input_path)):
        if file_name.endswith(".md"):
            pdf_path = os.path.join(input_path, file_name)
            output_path = os.path.join(ABSTRACTS_PATH, file_name)
            # Extract abstract from PDF and save to output_path
            logger.info(f"Extracting abstract from {pdf_path}")
            extract_single_abstract(pdf_path, output_path, index, total)
            # Add your PDF extraction logic here

def main():

    try:
        # Recreate the file if it exists
        os.remove(NOT_FOUND_ABSTRACT_FILE)
        # Create a new empty file
        with open(NOT_FOUND_ABSTRACT_FILE, 'w') as f:
            pass # Create an empty file
        logger.info(f"A new empty file '{NOT_FOUND_ABSTRACT_FILE}' has been created.")
    except FileNotFoundError:
        # If the file does not exist, create it directly
        with open(NOT_FOUND_ABSTRACT_FILE, 'w') as f:
            pass
        logger.info(f"The file '{NOT_FOUND_ABSTRACT_FILE}' did not exist and has been created empty.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    logger.info("Starting Abstract extraction...")
    extract_abstracts(RAW_DATA_PATH_MD_MISTRAL, ABSTRACTS_PATH)



if __name__ == "__main__":
    main()