# app/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app import ocr, parser, db
import os
import shutil

app = FastAPI()
UPLOAD_DIR = \"uploads/\"
os.makedirs(UPLOAD_DIR, exist_ok=True)

db.init_db()

@app.post(\"/upload_form\")
async def upload_form(file: UploadFile = File(...)):
    ext = file.filename.split(\".\")[-1].lower()
    if ext not in [\"png\", \"jpg\", \"jpeg\", \"pdf\"]:
        raise HTTPException(status_code=400, detail=\"Unsupported file type.\")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, \"wb\") as buffer:
        shutil.copyfileobj(file.file, buffer)

    raw_text = ocr.extract_text_from_image(file_path)
    structured = parser.structure_form_data(raw_text)
    db.save_form(file.filename, raw_text, structured)

    return {
        \"filename\": file.filename,
        \"summary\": structured
    }

@app.get(\"/form/{form_id}\")
async def get_form(form_id: int):
    row = db.get_form(form_id)
    if not row:
        raise HTTPException(status_code=404, detail=\"Form not found.\")
    return {
        \"filename\": row[1],
        \"raw_text\": row[2],
        \"structured\": row[3]
    }

@app.get(\"/forms\")
async def list_forms():
    forms = db.get_all_forms()
    return {\"forms\": [{\"id\": row[0], \"filename\": row[1]} for row in forms]}
