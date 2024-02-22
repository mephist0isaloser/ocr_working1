import main
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

UPLOAD_FOLDER = r"C:\Users\mohit\PycharmProjects\flaskProject\image_sauce"
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}

# Initialize the Watchdog event handler
class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        _, extension = os.path.splitext(event.src_path)
        if extension.lower() not in ALLOWED_EXTENSIONS:
            return

        image_path = event.src_path
        main.ocr_notes_summarizer(image_path)

if __name__ == "__main__":
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path=UPLOAD_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
