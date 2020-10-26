from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from time import sleep

from complier import compile_function

def watch(directory=os.getcwd()):

    # Since watchdog sometimes fires events multiple times, we'll only complie each path once per cycle
    compiled_this_cycle = {0}

    # Event which dispatches when a file or directory is modified
    def on_modified(event):
        # Ignore directories
        if event.is_directory: return

        path = event.src_path
        
        # Only compile .mcfunction files
        file_extension = os.path.splitext(path)[1]
        if file_extension != '.mcfunction': return

        # Check if this file has been compiled this cycle
        if path in compiled_this_cycle: return

        print(f'File \'{os.path.basename(path)}\' was modified, compiling if necessary...')
        compiled_this_cycle.add(path)

        # Wait for the text editors to finish writing to the file
        sleep(0.5)
        compile_function(path)


    event_handler = FileSystemEventHandler()
    event_handler.on_modified = on_modified

    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)

    print(f'Starting to watch for changes in \'{directory}\'.\nPress CTRL/CMD + C to terminate the process.')
    observer.start()

    # Watch loop
    try:
        while True:
            sleep(3)

            # Clear the compile list every cycle
            compiled_this_cycle.clear()
    
    # Terminate the process
    except KeyboardInterrupt:
        print('Killing the process...')
        observer.stop()
    
    observer.join()