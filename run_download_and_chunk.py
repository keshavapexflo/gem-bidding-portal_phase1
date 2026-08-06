"""Download current GeM bids and produce embedding-ready chunks.

This intentionally stops before the embedding stage.  Run it in Google Colab
for the initial import, then use ``bid_chunks.json`` with your embedding
workflow.
"""

from pathlib import Path

from downloading_v2 import main as download_new_bids
from gem_extract_and_chunks import process_directory


PROJECT_DIR = Path(__file__).resolve().parent
DOWNLOADS_DIR = PROJECT_DIR / "downloads"


def main() -> None:
    DOWNLOADS_DIR.mkdir(exist_ok=True)

    print("[1/2] Downloading newly listed GeM bid PDFs...", flush=True)
    download_new_bids()

    print("[2/2] Extracting bid metadata and creating chunks...", flush=True)
    process_directory(
        str(DOWNLOADS_DIR / "bids"),
        str(DOWNLOADS_DIR / "downloaded_bid_manifest.json"),
        str(PROJECT_DIR / "bid_chunks.json"),
        str(DOWNLOADS_DIR / "chunk_sync.json"),
    )
    print("Download and chunking complete. No embeddings were created.", flush=True)


if __name__ == "__main__":
    main()
