import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
import os
import sys
from dotenv import load_dotenv,dotenv_values
from docx import Document
from pdf2image import convert_from_path

from Extractor import OCR

load_dotenv()

start_time = time.time()

def open_by_file_source(script_path, src_path):
    call([sys.executable, script_path, src_path])

def open_by_file(script_path, src_path):
    call([sys.executable, script_path, src_path])

def do_myocr(img_path , ocr_model):
    image_path = rf"{img_path}"

    api_key = os.getenv("api_key_2")  # Replace with your API key
    # Create an instance of Gemini
    OCR.gemini_instance = OCR.Gemini(api_key)

    if (ocr_model==1):
        # Create an instance of EasyOcr and Apply it
        OCR.easyocr_instance = OCR.EasyOcr()
        OCR.extracted_text = OCR.easyocr_instance.apply_ocr(image_path)
    elif(ocr_model==2):
        # Create an instance of Doctor OCR
        OCR.DoctrOCR_instance = OCR.DoctrOCR()
        OCR.extracted_text =OCR.DoctrOCR_instance.apply_ocr(image_path)
    elif(ocr_model==3):
        # Create an instance of SuryaOcr OCR
        OCR.TesseractOCR_instance = OCR.TesseractOCR()
        OCR.extracted_text =OCR.TesseractOCR_instance.apply_ocr(image_path)
    else:
        # Create an instance of Paddle OCR
        OCR.PaddleOCR_instance = OCR.Paddle_OCR()
        OCR.extracted_text =OCR.PaddleOCR_instance.apply_ocr(image_path)

    # Generate response from Gemini model
    response_text = OCR.gemini_instance.generate_response(OCR.extracted_text)
    return response_text    

def main():
    try:
        file_path = sys.argv[1]
        extracted_text=do_myocr(file_path , 3)
        open_by_file(rf"D:\Grad\OCR-RPA\Document_fill\json_to_doc_ui.py",extracted_text)
        open_by_file(rf"D:\Grad\OCR-RPA\CSV_fill\jcsv_ui.py",extracted_text)
        return f"total:,{time.time()-start_time}"
    except Exception as e:
        return 'skipped'

print(main())