import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

WATCH_FOLDER = "C:/Users/Shahzeb/OneDrive/Desktop/assignment_5/input"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"📂 File arrived: {event.src_path}")
            subprocess.run(["python", "export_data.py"])

if __name__ == "__main__":
    os.makedirs(WATCH_FOLDER, exist_ok=True)
    observer = Observer()
    observer.schedule(FileEventHandler(), path=WATCH_FOLDER, recursive=False)
    observer.start()
    print("📡 Monitoring for new files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
