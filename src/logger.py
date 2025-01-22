import logging   # logging: A module for handling logging in Python. It’s used to record messages (info, warnings, errors, etc.) in a structured way.
import os #  A module for interacting with the operating system. Here, it helps with creating directories and managing file paths

from datetime import datetime
# datetime.now(): Gets the current date and time (e.g., 2025-01-22 14:23:45).
# .strftime('%m_%d_%Y_%H_%M_%S'): Converts the datetime object into a string with the format

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# It will go from this -> 2025-01-22 14:23:45        to this       -> "01_22_2025_14_23_45.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
""" os.getcwd(): Gets the current working directory (CWD), i.e., the directory where the script is running.
 os.path.join(): Joins directory and file names into a valid path for the operating system.
 "logs": The directory where log files will be stored.
 LOG_FILE: The name of the log file.
 logs_path = "/home/user/project/logs/01_22_2025_14_23_45.log" if os.getcwd is /home/user/project.
"""
os.makedirs(logs_path,exist_ok=True) #If the directory already exists, it won’t raise an error.

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) 
'''The basicConfig function is used to configure the logging system. It sets up the basic behavior for logging in your program, such as:
Where logs are stored.
How logs are formatted.
The minimum log level to be recorded.
'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
)

if __name__=="__main__":
    logging.info("Logging has started")