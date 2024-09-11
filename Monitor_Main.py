import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
import os
import sys
from dotenv import load_dotenv,dotenv_values

from Extractor import OCR

start_time = time.time()

def open_by_file_source(script_path, src_path):
    call(["python", script_path, src_path])

def open_by_file(script_path, src_path):
    call(["python", script_path, src_path])

def do_myocr(img_path):
    image_path = rf"{img_path}"
    api_key = os.getenv("api_key")  # Replace with your API key
    # Create an instance of Gemini
    OCR.gemini_instance = OCR.Gemini(api_key)
    # Create an instance of EasyOcr
    OCR.easyocr_instance = OCR.EasyOcr()
    # Apply OCR to the image
    OCR.extracted_text = OCR.easyocr_instance.apply_ocr(image_path)
    # Generate response from Gemini model
    response_text = OCR.gemini_instance.generate_response(OCR.extracted_text)
    return response_text


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'File created: {event.src_path}')
        time_now = time.time()

        extracted_text=do_myocr(event.src_path)
        
        print("first file" ,time.time() - time_now)
        time_now = time.time()

        open_by_file(r"..\OCR-RPA\Document_fill\json_to_doc.py",extracted_text)
        open_by_file(r"..\CSV_fill\jcsv.py",extracted_text)

        print("second file" ,time.time() - time_now)
        print("total:",time.time()-start_time)


if __name__ == "__main__":
    path = r"..\OCR-RPA\imgs"  # Folder to monitor
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
         while True:
             time.sleep(1)
    except KeyboardInterrupt:
         observer.stop()
    observer.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")