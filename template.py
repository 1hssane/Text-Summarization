import os
from pathlib import Path
import logging

logging.basicConfig (level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="text-summarization"
list_of_files =[
    #deployement
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    # Convert path to Path object
    filepath = Path(filepath)
    # Separate directory and filename
    filedir,filename = os.path.split(filepath)
    # Create directory if it doesn't exist (with error handling)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the  file name {filename}")
    # Create or empty file if necessary
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass # No content needed for empty files
            logging.info(f"Creating empty file : {filepath}")
    
    else :

        logging.info(f"File already exists : {filename}")