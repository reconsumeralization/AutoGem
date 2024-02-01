# Update the test_watcher.py script with the integration for the testing factory
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class TestingFactory:
    @staticmethod
    def handle_file_change(file_path):
        # Simulated implementation for demonstration
        print(f"Simulated testing factory handling file change for: {file_path}")

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File changed: {event.src_path}')
        # Call the simulated testing factory's handle_file_change method
        TestingFactory.handle_file_change(event.src_path)

def start_watching(path='app/'):
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()