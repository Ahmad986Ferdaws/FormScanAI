# app/ocr.py

import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f\"OCR failed: {e}\")
        return \"\"

if __name__ == \"__main__\":
    text = extract_text_from_image(\"uploads/form1.png\")
    print(\"Raw OCR Output:\\n\", text)
