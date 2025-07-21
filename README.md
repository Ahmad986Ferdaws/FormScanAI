# FormScanAI

FormScanAI lets you upload scanned documents and automatically extracts & structures the form data using OCR + GPT.

## Features
- Upload scans or photos
- OCR text extraction (Tesseract)
- GPT-4 data structuring
- SQLite storage
- JSON output

## Setup
1. Install Tesseract (`brew install tesseract` or `apt install tesseract-ocr`)
2. Add `.env` with your OpenAI API key
3. Install: `pip install -r requirements.txt`
4. Run: `uvicorn app.main:app --reload`
