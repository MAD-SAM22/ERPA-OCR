import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
import os
import itertools
import sys
from dotenv import load_dotenv,dotenv_values


from Extractor import OCR


# Load the keys from the environment variable and split into a list
api_keys = os.getenv('api_keys').split(', ')
api_key_iterator = itertools.cycle(api_keys)

#Start total time for calculating the whole project time
start_time = time.time()

def open_by_file_source(script_path, src_path):
    call([sys.executable, script_path, src_path])

def open_by_file(script_path, src_path):
    call([sys.executable, script_path, src_path])

def do_myocr(img_path, ocr_model):
    image_path = rf"{img_path}"

    while True:
        try:
            # Get the next API key from the iterator
            api_key = next(api_key_iterator)
            print(f"Using API key: {api_key}")

            # Create an instance of Gemini with the current API key
            OCR.gemini_instance = OCR.Gemini_BID(api_key)

            if ocr_model == 1:
                # Create an instance of EasyOcr and Apply it
                OCR.easyocr_instance = OCR.EasyOcr()
                OCR.extracted_text = OCR.easyocr_instance.apply_ocr(image_path)
            elif ocr_model == 2:
                # Create an instance of Doctr OCR
                OCR.DoctrOCR_instance = OCR.DoctrOCR()
                OCR.extracted_text = OCR.DoctrOCR_instance.apply_ocr(image_path)
            elif ocr_model == 3:
                # Create an instance of Tesseract OCR
                OCR.TesseractOCR_instance = OCR.TesseractOCR()
                OCR.extracted_text = OCR.TesseractOCR_instance.apply_ocr(image_path,'por')
            else:
                # Create an instance of Paddle OCR
                OCR.PaddleOCR_instance = OCR.Paddle_OCR()
                OCR.extracted_text = OCR.PaddleOCR_instance.apply_ocr(image_path)

            # Generate response from Gemini model
            response_text = OCR.gemini_instance.generate_response(OCR.extracted_text)
            return response_text

        except Exception as e:
            print(f"Error with API key {api_key}: {e}")
            print("Switching to the next API key...")
            # The loop will continue and try the next key from the list


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'File created: {event.src_path}')
        time_now = time.time()
        try:
            extracted_text=do_myocr(event.src_path , 4)
            print("first file" ,time.time() - time_now)
            time_now = time.time()
            open_by_file(rf"..\OCR-RPA\Document_fill\json_to_doc_BID.py",extracted_text)
            open_by_file(rf"..\OCR-RPA\CSV_fill\jcsv_BID.py",extracted_text)
            print("second file" ,time.time() - time_now)
            print("total:",time.time()-start_time)
        except Exception as e:
            print(e)

      


if __name__ == "__main__":
    path = rf"..\OCR-RPA\imgs"  # Folder to monitor
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("monitoring...")
    try:
         while True:
             time.sleep(1)
    except KeyboardInterrupt:
         observer.stop()
    observer.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")