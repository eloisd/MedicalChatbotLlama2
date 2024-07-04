import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

list_of_files = ["src/__init__.py",
                 "src/helper.py",
                 "src/prompts.py",
                #  ".env",
                 "setup.py",
                 "research/trials.ipynb",
                 "app.py",
                 "store_index.py",
                 "static/.gitignore",
                 "templates/chat.html"
                 ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename =os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"File created: {filename}")
    else:
        logging.info(f"File already exists: {filename}")