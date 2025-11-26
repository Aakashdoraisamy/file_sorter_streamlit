import os
import shutil
from pathlib import Path
from datetime import datetime
import logging
from config import FILE_TYPES

log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)
logging.basicConfig(filename=log_folder / "file_log.txt", level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def sort_files(folder_path):
    folder = Path(folder_path)
    moved_files = []

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:

                    file_date = datetime.fromtimestamp(file.stat().st_mtime)
                    dest_folder = folder / category / f"{file_date.year}-{file_date.month:02}"
                    dest_folder.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file), dest_folder / file.name)
                    moved_files.append(f"{file.name} → {category}/{file_date.year}-{file_date.month:02}")
                    logging.info(f"Moved {file.name} to {category}/{file_date.year}-{file_date.month:02}")
                    moved = True
                    break

            if not moved:
                other_folder = folder / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), other_folder / file.name)
                moved_files.append(f"{file.name} → Others")
                logging.info(f"Moved {file.name} to Others")
    
    return moved_files
