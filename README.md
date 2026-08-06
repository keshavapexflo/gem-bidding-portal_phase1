# GeM download and chunking for Colab

This folder contains only the initial ingestion steps:

```text
GeM portal -> PDF downloads -> bid_chunks.json
```

It deliberately does **not** create embeddings or a Chroma database. You can
create those in Colab, then return the resulting `chroma_db/` folder here and
use the included Streamlit search app locally.

## Run in Google Colab

1. Upload this whole folder to a Google Drive location, then mount Drive in Colab.
2. Change to the uploaded folder and install the two required packages:

   ```python
   %cd /content/drive/MyDrive/gem-bidding-colab-ingestion
   !pip install -r requirements.txt
   ```

3. Run the ingestion pipeline:

   ```python
   !python run_download_and_chunk.py
   ```

On a fresh folder, the downloader scans every currently ongoing GeM bid. On a later run, `downloads/downloaded_bid_manifest.json` lets it download only newly listed bids.

## Outputs to keep

- `downloads/bids/` - downloaded PDFs
- `downloads/downloaded_bid_manifest.json` - remembers downloaded bid IDs
- `bid_chunks.json` - the embedding-ready chunks
- `downloads/chunk_sync.json` - IDs of new, changed, and removed chunks

Keep these files together. They are needed if you later want local incremental downloading and chunking without reprocessing the initial dataset.

## Use the app after embedding

After your Colab embedding job finishes, copy its `chroma_db/` output into
this folder. Keep the local `downloads/` folder and `bid_chunks.json` in place.
Then install the requirements on the laptop and start the app:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The app files are `app.py`, `gem_hybrid_retrieval.py`, and
`gem_live_status.py`. They search the local `chroma_db/` collection; they do
not create corpus embeddings.
