import os
import pandas as pd
import time
import datetime
import requests
import sys
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote_plus
from typing import List
from LoggerSetUp import setup_logger

from config import(
    RAW_DATA_PATH_PDF,
    PDF_METADATA_PATH,
    BIBLIOGRAPHY_APA_FILE,
    BIBLIOGRAPHY_TITLES_FOLDER,
    RESULTS_FOLDER,
    EMAIL,
    LOGS_BASE_PATH,
    LOG_LEVEL
)

# Configure logger
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='APABibliographyDownload.log',
    error_log_filename='APABibliographyDownload_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)

# Extract titles from bibliography
def extract_titles(bibliography: List[str]) -> List[str]:
    """
    Extracts the titles from a list of bibliography entries using a regular expression.
    
    Args:
        bibliography (List[str]): List of bibliography entries as strings.
    
    Returns:
        List[str]: List of extracted titles. If a title is not found, a placeholder is added.
    """
    titles = []
    for entry in bibliography:
        # Search for the text after the first "). " up to the next ". [A-Z]"
        match = re.search(r'.*?\)\.\s+([^.]+)\..*', entry)
        if match:
            title = match.group(1).strip()
            titles.append(title)
            logger.debug(f"Extracted title: {title}")
        else:
            titles.append("[TITLE NOT FOUND]")
            logger.warning(f"Title not found in entry: {entry}")
    logger.info(f"Extracted {len(titles)} titles from bibliography.")
    return titles

# Save titles to file
def save_titles_to_file(titles: List[str], output_file: str) -> None:
    """
    Saves the extracted titles to a text file.

    Args:
        titles (List[str]): List of extracted titles.
        output_file (str): Path to the output file.
    """
    # Save results
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for title in titles:
                f.write(title + '\n')
        logger.info(f"Extracted {len(titles)} titles to '{output_file}'.")
        print(f"{len(titles)} titles have been extracted to '{output_file}'.")
    except Exception as e:
        logger.error(f"Error writing output file: {e}")
        sys.exit(1)

# Read titles from file
def read_titles(filepath: str) -> List[str]:
    """
    Read and return a list of non-empty titles from a file.

    Args:
        filepath (str): The path to the file to read.

    Returns:
        List[str]: A list of non-empty titles.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        logger.error(f"Failed to read titles from {filepath}: {e}")
        return []

  
# Query Unpaywall API
def query_unpaywall(title, email):
    """
    Queries the Unpaywall API to retrieve an open-access PDF link if available.

    Parameters:
        title (str): The title of the article.
        email (str): The user's email for API access.

    Returns:
        tuple: (pdf_url, is_direct_pdf) - URL and whether it's a direct PDF or landing page
    """
    query = quote_plus(title)
    api_url = f"https://api.unpaywall.org/v2/search?query=\"{query}\"&email={email}"
    
    try:
        # Call Unpaywall API
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()["results"][0]['response']

        # If the response contains "results", use the first one
        if isinstance(data, dict) and "results" in data:
            if isinstance(data["results"], list) and len(data["results"]) > 0:
                data = data["results"][0]
            else:
                return None, False
        
        # Check if the best OA location is available
        if data and "best_oa_location" in data:
            if data["best_oa_location"].get("url_for_pdf"):
                return data["best_oa_location"]["url_for_pdf"], True
            elif data["best_oa_location"].get("url_for_landing_page"):
                return data["best_oa_location"]["url_for_landing_page"], False
        
        return None, False

    except requests.exceptions.RequestException as e:
        logger.error(f"Unpaywall API error: {e}", flush=True)
        return None, False

# Scrape for PDF links
def scrape_for_pdf(url):
    """
    Attempts to find a PDF download link by scraping the article's landing page.

    Parameters:
        url (str): The URL of the article's landing page.

    Returns:
        str: PDF download link if found, otherwise None.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        logger.info(f"Accessing landing page: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        logger.info(f"  Searching for download links in landing page...")
        # Search for links that might lead to a PDF
        pdf_candidates = []
        
        for link in soup.find_all("a", href=True):
            # Get the href attribute and link text
            href = link["href"]
            link_text = link.get_text().lower().strip()
            
            # Check different patterns that might indicate a PDF link
            if (href.endswith(".pdf") or 
                "pdf" in href.lower() or 
                "download" in href.lower() or 
                "fulltext" in href.lower() or
                "download" in link_text or 
                "pdf" in link_text or
                "full text" in link_text):
                
                # Convert relative URLs to absolute URLs
                full_url = href if href.startswith(("http://", "https://")) else urljoin(url, href)
                pdf_candidates.append((full_url, link_text))
        
        # If we found candidates, log them and return the first one
        if pdf_candidates:
            print(f"  Found {len(pdf_candidates)} potential download links", flush=True)
            logger.info(f"  Found {len(pdf_candidates)} potential download links")
            for i, (candidate_url, text) in enumerate(pdf_candidates[:3]):  # Show at most 3 candidates
                logger.info(f"  Candidate {i+1}: {text} -> {candidate_url[:80]}{'...' if len(candidate_url) > 80 else ''}")

            # Return the first candidate
            return pdf_candidates[0][0]
        else:
            logger.info(f"  No download links found on the landing page")
            return None
            
    except requests.exceptions.RequestException as e:
        logger.error(f"  [ERROR] Failed to access landing page: {e}")
        return None
    except Exception as e:
        logger.error(f"  [ERROR] Error during web scraping: {e}")
        return None

# Download PDF
def download_pdf(url, title, output_dir):
    """
    Downloads the PDF from a given URL and saves it to a specified directory.

    Parameters:
        url (str): Direct link to the PDF file.
        title (str): Title of the article (used for naming the file).
        output_dir (str): Directory where the PDF will be saved.

    Returns:
        str: "Success" if the download is completed, otherwise an error message.
    """
    if not url:
        return "No PDF URL found"
    
    # Ensure the filename is valid and avoid special characters
    filename = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)[:100] + ".pdf"
    file_path = os.path.join(output_dir, filename.replace("..", "_"))
    
    os.makedirs(output_dir, exist_ok=True)

    if os.path.exists(file_path):
        return "File already exists"
    
    try:
        # Download the PDF
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()
        
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return "Success"
    except requests.exceptions.RequestException as e:
        return f"Failed to download PDF: {e}"

# Download article with fallback
def download_article_with_fallback(title:str, email:str, output_dir:str) -> dict:
    """
    Attempts to download an article using Unpaywall API.
    If Unpaywall returns a landing page URL, tries to scrape it for PDF links.

    Parameters:
        title (str): Title of the article.
        email (str): User email for Unpaywall API.
        output_dir (str): Directory to save the PDFs.

    Returns:
        dict: Dictionary containing the status and reason of the download attempt.
    """
    result = {
        "DOI": None, 
        "Article Title": title, 
        "Status": "Failed", 
        "Reason": None
    }

    title = title
    logger.info(f"Processing: {title[:50]}{'...' if len(title) > 50 else ''}")

    try:
        # Attempt Unpaywall
        logger.info(f"  Querying Unpaywall API...")
        pdf_url, is_direct_pdf = query_unpaywall(title, email)
        
        if pdf_url:
            if is_direct_pdf:
                logger.info(f"  Found direct PDF URL: {pdf_url[:80]}{'...' if len(pdf_url) > 80 else ''}")
                reason = download_pdf(pdf_url, title, output_dir)
            else:
                logger.info(f"  Found landing page URL, not a direct PDF")
                # Try to find a download link on the landing page
                download_link = scrape_for_pdf(pdf_url)
                if download_link:
                    logger.info(f"  Found download link from landing page: {download_link[:80]}{'...' if len(download_link) > 80 else ''}")
                    reason = download_pdf(download_link, title, output_dir)
                else:
                    reason = "No PDF download link found on landing page"
            
            result["Reason"] = reason
            if reason == "Success":
                print(f"  Download successful!", flush=True)
                result["Status"] = "Success"

        else:
            logger.info(f"  No accessible PDF found in Unpaywall")
            result["Reason"] = "No accessible PDF found in Unpaywall"

        # If the download was successful, save metadata as JSON
        if result["Reason"] in ["Success", "File already exists"]:
            safe_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)[:100]
            json_filename = safe_title + ".json"
            json_dir = PDF_METADATA_PATH
            os.makedirs(json_dir, exist_ok=True)
            json_path = os.path.join(json_dir, json_filename)

            if not os.path.exists(json_path):
                try:
                    query = quote_plus(title)
                    api_url = f"https://api.unpaywall.org/v2/search?query=\"{query}\"&email={email}"
                    response = requests.get(api_url, timeout=10)
                    response.raise_for_status()
                    data = response.json()["results"][0]['response']

                    # If the response contains "results", use the first one
                    if isinstance(data, dict) and "results" in data and isinstance(data["results"], list):
                        if len(data["results"]) > 0:
                            data = data["results"][0]
                        else:
                            data = {}

                    with open(json_path, 'w', encoding='utf-8') as f:
                        import json
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    logger.info(f"  Metadata JSON saved to {json_path}")
                except Exception as e:
                    logger.warning(f"  [WARNING] Could not save metadata JSON: {e}")

        return result

    except Exception as e:
        error_message = f"Unexpected error: {e}"
        logger.error(f"  Error: {error_message}")
        result["Reason"] = error_message
        return result

def main():

    input_file = BIBLIOGRAPHY_APA_FILE
    output_file = os.path.join(BIBLIOGRAPHY_TITLES_FOLDER, BIBLIOGRAPHY_APA_FILE.split('/')[-1].replace('.txt', '_titles.txt'))
    email_input = EMAIL
    failed_dir = RESULTS_FOLDER

    logger.info(f"Reading bibliography entries from '{input_file}'.")

    # Read lines from the input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        logger.info(f"Read {len(lines)} entries from input file.")
    except Exception as e:
        logger.error(f"Error reading input file: {e}")
        sys.exit(1)

    # Extract titles
    titles = extract_titles(lines)

    # Save results
    save_titles_to_file(titles, output_file)

    start_time = datetime.datetime.now()
    separator = "=" * 80

    logger.info(f"\n{separator}")
    logger.info(f"Starting PDF download process at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"{separator}\n")

    try:
        titles = read_titles(output_file)
        logger.info(f"Found {len(titles)} titles to process.")
        total_articles=len(titles)
        # Define output directory
        output_directory = RAW_DATA_PATH_PDF
        logger.info(f"Output directory: {output_directory}")

        # Ensure output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Ensure failed downloads directory exists
        
        os.makedirs(failed_dir, exist_ok=True)

        
        failed_downloads = []
        successful_downloads = 0

        logger.info(f"\n{separator}")
        logger.info("Starting download process...")
        logger.info(f"{separator}\n")

        for index, row in enumerate(titles):
            progress = (index + 1) / total_articles * 100
            logger.info(f"[{index + 1}/{total_articles}] - {progress:.1f}% Complete")

            try:
                # Attempt to download the article
                if not row:
                    logger.warning(f"  Missing Title for article: {row}")
                    failed_downloads.append({
                        "Index": index,
                        "DOI": "Missing",
                        "Article Title": row,
                        "Status": "Failed",
                        "Reason": "Missing Title"
                    })
                    continue
                    
                result = download_article_with_fallback(row, email_input, output_directory)
                if result["Status"] == "Failed":
                    result["Index"] = index
                    failed_downloads.append(result)
                else:
                    successful_downloads += 1
            except Exception as e:
                error_message = f"Unexpected error: {e}"
                logger.error(f"  Error: {error_message}")
                failed_downloads.append({
                    "Index": index,
                    "DOI": None,
                    "Article Title": row,
                    "Status": "Failed",
                    "Reason": error_message
                })
            
            # Sleep between requests to avoid rate limiting
            time.sleep(0.5)
        
        # Save failed download attempts to a CSV file for debugging
        end_time = datetime.datetime.now()
        duration = end_time - start_time

        logger.info(f"\n{separator}")
        logger.info(f"Download process completed at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Total execution time: {duration}")
        logger.info(f"Results summary:")
        logger.info(f"  - Total articles processed: {total_articles}")
        logger.info(f"  - Successfully downloaded: {successful_downloads} ({successful_downloads/total_articles*100:.1f}%)")
        logger.info(f"  - Failed to download: {len(failed_downloads)} ({len(failed_downloads)/total_articles*100:.1f}%)")

        if failed_downloads:
            failed_df = pd.DataFrame(failed_downloads)
            failed_path = os.path.join(failed_dir, 'failed_bibliography_downloads.csv')
            failed_df.to_csv(failed_path, index=False)
            logger.info(f"Failed download attempts have been saved to: {failed_path}")

        logger.info(f"{separator}\n")

    except Exception as e:
        logger.error(f"Critical error in main process: {e}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()