# LOGGING 
import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        #We want to see the file(here running_logs),
        #Also we want to see the log in terminal
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
#Create a logger object by name cnnClassifierLogger
logger=logging.getLogger("cnnClassifierLogger")
