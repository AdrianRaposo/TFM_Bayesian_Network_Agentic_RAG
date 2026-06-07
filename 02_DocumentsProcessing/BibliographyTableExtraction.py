import re
import os
import datetime
import json
from LoggerSetUp import setup_logger


from config import(
    RAW_DATA_PATH_MD_MISTRAL,
    CLEANED_DATA_PATH,
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

# Reference Patterns
REF_HEADER_PATTERNS = [
    r"(?:^|\n)#{1,4}\s*(\*\*|\*)?\s*References?\s*(\*\*|\*)?\s*\n",
    r"(?:^|\n)#{1,4}\s*(\*\*|\*)?\s*Bibliography\s*(\*\*|\*)?\s*\n",
    r"(?:^|\n)#{1,4}\s*\d+\.?\s*REFERENCES?\s*\n",      # numbered
    r"(?:^|\n)#{1,4}\s*[IVX]+\.\s*REFERENCES?\s*\n",   # roman numerals
]


def extract_references_section(md_content: str) -> dict:
    """
    Extract references/bibliography section as structured dict.

    Args:
        md_content (str): The markdown content to search within.

    Returns:
        dict: A dictionary containing the extracted references/bibliography section.
    """

    for pattern in REF_HEADER_PATTERNS:
        match = re.search(pattern, md_content, re.IGNORECASE)
        if match:
            start_pos = match.start()
            content_start = match.end()
            next_header = re.search(r"\n#{1,4}\s+", md_content[content_start:])
            end_pos = content_start + next_header.start() if next_header else len(md_content)

            ref_content = md_content[content_start:end_pos].strip()
            references = extract_individual_references(ref_content)

            return {
                "header": match.group(0).strip(),
                "content": ref_content,
                "references": references,
                "reference_count": len(references),
            }
    return None


def remove_references_section(md_content: str) -> str:
    """
    Remove references/bibliography section.

    Args:
        md_content (str): The markdown content to modify.

    Returns:
        str: The modified markdown content without the references/bibliography section.
    """
    for pattern in REF_HEADER_PATTERNS:
        match = re.search(pattern, md_content, re.IGNORECASE)
        if match:
            start_pos = match.start()
            content_start = match.end()
            next_header = re.search(r"\n#{1,4}\s+", md_content[content_start:])
            end_pos = content_start + next_header.start() if next_header else len(md_content)
            return md_content[:start_pos] + md_content[end_pos:]
    return md_content


def extract_individual_references(ref_content: str) -> list:
    """
    Split reference block into individual references.

    Args:
        ref_content (str): The reference content to split.

    Returns:
        list: A list of individual references extracted from the content.
    """
    patterns = [
        r"(?:^|\n)\[(\d+)\]\s+(.*?)(?=\n\[\d+\]|\n\n|$)",  # [1] Author...
        r"(?:^|\n)(\d+)\.\s+(.*?)(?=\n\d+\.|\n\n|$)",      # 1. Author...
        r"(?:^|\n)-\s+(.*?)(?=\n-|\n\n|$)",                # - Author...
        r"(?:^|\n)([A-Z][^#\n]+?)(?=\n[A-Z]|\n\n|$)",      # fallback
    ]
    for pat in patterns:
        matches = re.finditer(pat, "\n" + ref_content, re.MULTILINE | re.DOTALL)
        refs = []
        for m in matches:
            if len(m.groups()) == 2:
                num, text = m.groups()
                refs.append({"ref_id": num, "text": text.strip()})
            else:
                refs.append({"ref_id": str(len(refs)+1), "text": m.group(1).strip()})
        if refs:
            return refs
    # fallback: line split
    return [{"ref_id": str(i+1), "text": line} for i, line in enumerate(ref_content.splitlines()) if line.strip()]



# Tables
def extract_tables(md_content: str) -> list:
    """
    Extract markdown tables into structured JSON-like objects.

    A table is defined by its header and rows, and can span multiple lines.

    Args:
        md_content (str): The markdown content to search within.

    Returns:
        list: A list of extracted tables, each represented as a dictionary.
    """
    lines = md_content.split("\n")
    tables, current, in_table = [], [], False
    table_title, table_number = None, None

    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "|" in line[1:]:
            if not in_table:
                in_table = True
                # Look back for title
                for j in range(max(0, i-5), i):
                    prev = lines[j].strip()
                    m = re.match(r"^Table\s+(\d+)[.:]\s*(.*)$", prev, re.IGNORECASE)
                    if m:
                        table_number, table_title = m.group(1), m.group(2)
                        break
            current.append(line)
        elif in_table:
            if not line.strip().startswith("|"):
                if len(current) >= 3:
                    tables.append((table_number, table_title, current))
                current, in_table, table_title, table_number = [], False, None, None

    # process tables
    results = []
    for num, title, lines in tables:
        headers = [h.strip() for h in lines[0].split("|")[1:-1]]
        rows = []
        for row in lines[2:]:
            cells = [c.strip() for c in row.split("|")[1:-1]]
            if len(cells) == len(headers):
                rows.append(cells)
        results.append({
            "table_number": num,
            "table_title": title,
            "headers": headers,
            "rows": rows,
            "row_count": len(rows),
            "column_count": len(headers),
        })
    return results


def remove_tables(md_content: str) -> str:
    """
    Remove all markdown tables (lines starting with |).

    Args:
        md_content (str): The markdown content to process.

    Returns:
        str: The cleaned markdown content without tables.
    """
    lines, out, in_table = md_content.split("\n"), [], False
    for line in lines:
        if line.strip().startswith("|") and "|" in line[1:]:
            in_table = True
            continue
        elif in_table and not line.strip().startswith("|"):
            in_table = False
        if not in_table:
            out.append(line)
    return "\n".join(out)


def main(input_dir: str, output_dir: str):

    logger.info(f"Starting extraction from {input_dir} to {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "CLEANED_MD"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "JSON_BIBLIOGRAPHY_AND_TABLES"), exist_ok=True)

    for root, _, files in os.walk(input_dir):
        for i, fname in enumerate(files):
            logger.info(f"Processing file {i+1}/{len(files)}: {fname}")
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)

            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            # --- extract ---
            logger.info(f"Extracting references and tables from {fname}")
            refs = extract_references_section(content)
            tables = extract_tables(content)
            # --- clean content ---
            cleaned = content
            if refs:
                cleaned = remove_references_section(cleaned)
            if tables:
                cleaned = remove_tables(cleaned)

            # --- save cleaned markdown ---
            rel_path = os.path.relpath(fpath, input_dir)
            out_path = os.path.join(output_dir, "CLEANED_MD", rel_path)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(cleaned)

            # --- build JSON for this paper ---
            paper_json = {
                "extraction_date": datetime.datetime.now().isoformat(),
                "file": fname,
                "references": refs,
                "tables": tables,
            }

            # --- save JSON ---
            json_out = os.path.join(output_dir, "JSON_BIBLIOGRAPHY_AND_TABLES", fname.replace(".md", ".json"))
            with open(json_out, "w", encoding="utf-8") as f:
                json.dump(paper_json, f, indent=2, ensure_ascii=False)

            logger.info(f"Processed {fname}  JSON + cleaned Markdown saved.")


if __name__ == "__main__":
    # Example usage:
    input_dir = RAW_DATA_PATH_MD_MISTRAL
    output_dir = CLEANED_DATA_PATH
    main(input_dir, output_dir)

