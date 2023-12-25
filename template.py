import os
from pathlib import Path
import logging


logging .basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name="cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]
for fp in list_of_files:
    fp=Path(fp)
    fd,file_name=os.path.split(fp)
    
    if fd !="":
        os.makedirs(fd,exist_ok=True)
        logging.info(f"Created dir; {fd} for the file {file_name}")
    if not(os.path.exists(fp)) or (os.path.getsize(fp)==0):
        with open(fp,"w") as f:
            pass
            logging.info(f"Created empty file :{fp}")
    else:
        logging.info(f"{file_name} is already exists")        
                

