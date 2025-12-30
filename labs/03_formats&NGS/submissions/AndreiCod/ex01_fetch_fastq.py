"""
Exercise 03 — FASTQ Download (student-owned)

Objective:
- Choose a TP53-related accession (e.g., SRR..., ERR...) and DOWNLOAD a FASTQ file.
- Save it in data/work/<handle>/lab03/your_reads.fastq.gz

Minimum requirements:
- The script must accept an accession (e.g., from command line args).
- The script downloads at least one FASTQ (one file is enough for the exercise).
- The script prints to stdout the path of the downloaded file.

Recommended:
- Support .fastq or .fastq.gz.

NOTE:
- The chosen library does not matter (requests/urllib/etc.), but avoid heavy packages.
"""

import sys
import os
import subprocess
from pathlib import Path

# GitHub handle
HANDLE = "AndreiCod"

# Output directory
OUT_DIR = Path(f"data/work/{HANDLE}/lab03")


def get_fastq_url(accession: str) -> str:
    """
    Query ENA Portal API to get the FASTQ download URL for a given accession.
    Returns the first FASTQ FTP URL found.
    """
    import urllib.request

    api_url = (
        f"https://www.ebi.ac.uk/ena/portal/api/filereport?"
        f"accession={accession}&result=read_run&fields=fastq_ftp"
    )

    with urllib.request.urlopen(api_url) as response:
        content = response.read().decode("utf-8")

    # Parse TSV response: first line is header, second line has data
    lines = content.strip().split("\n")
    if len(lines) < 2:
        raise ValueError(f"No FASTQ found for accession: {accession}")

    # Format: run_accession\tfastq_ftp
    # fastq_ftp may contain multiple URLs separated by semicolons
    data_line = lines[1]
    parts = data_line.split("\t")
    if len(parts) < 2 or not parts[1]:
        raise ValueError(f"No FASTQ URL in response for accession: {accession}")

    # Take the first URL (there may be multiple for paired-end reads)
    ftp_urls = parts[1].split(";")
    ftp_url = ftp_urls[0].strip()

    # Prepend protocol if missing - use HTTP as FTP may not work with urllib
    if not ftp_url.startswith("http") and not ftp_url.startswith("ftp://"):
        # ENA provides URLs without protocol, use HTTP for better compatibility
        ftp_url = "http://" + ftp_url

    return ftp_url


def download_file(url: str, output_path: Path) -> None:
    """
    Download a file from URL to the specified output path using wget or curl.
    """
    print(f"Downloading from: {url}")
    print(f"Saving to: {output_path}")

    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Use wget or curl for robust downloading
    try:
        # Try wget first
        result = subprocess.run(
            ["wget", "-q", "--show-progress", "-O", str(output_path), url], check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fall back to curl
        try:
            result = subprocess.run(
                ["curl", "-L", "-o", str(output_path), url], check=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(
                f"Neither wget nor curl available or download failed: {e}"
            )


def main():
    # Read accession from command line
    if len(sys.argv) < 2:
        print("Usage: python ex01_fetch_fastq.py <accession>")
        print("Example: python ex01_fetch_fastq.py ERR000001")
        sys.exit(1)

    accession = sys.argv[1]
    print(f"Fetching FASTQ for accession: {accession}")

    # Query ENA for FASTQ URL
    try:
        fastq_url = get_fastq_url(accession)
    except Exception as e:
        print(f"Error querying ENA: {e}")
        sys.exit(1)

    # Determine output filename
    # Use the original filename from URL, or default to your_reads.fastq.gz
    url_filename = fastq_url.split("/")[-1]
    if url_filename.endswith(".fastq.gz") or url_filename.endswith(".fastq"):
        output_file = OUT_DIR / "your_reads.fastq.gz"
    else:
        output_file = OUT_DIR / "your_reads.fastq.gz"

    # Download the file
    try:
        download_file(fastq_url, output_file)
    except Exception as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

    print(f"Downloaded: {output_file.resolve()}")


if __name__ == "__main__":
    main()
