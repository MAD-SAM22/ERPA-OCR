import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
import os
import sys

from Extractor import OCR

start_time = time.time()

def open_by_file_source(script_path, src_path):
    call(["python", script_path, src_path])

def open_by_file(script_path, src_path):
    call(["python", script_path, src_path])

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File modified: {event.src_path}')

    def on_created(self, event):
        print(f'File created: {event.src_path}')
        time_now = time.time()
        open_by_file_source(r'C:\\Users\\omarn\\Documents\\Grad\\OCR+FormatFilling\\OCR\\ocr_to_json.py', event.src_path)
        print("first file" ,time.time() - time_now)
        time_now = time.time()
        open_by_file(r'C:\\Users\\omarn\\Documents\\Grad\\OCR+FormatFilling\\Document_fill\\document_filling.py',event.src_path)
        print("second file" ,time.time() - time_now)
        print("total:",time.time()-start_time)

    def on_deleted(self, event):
        print(f'File deleted: {event.src_path}')

    def on_moved(self, event):
        print(f'File moved: {event.src_path} to {event.dest_path}')

if __name__ == "__main__":
    path = r'C:\\Users\\omarn\\Documents\\Grad\\OCR+FormatFilling\\OCR\\img'  # Folder to monitor
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