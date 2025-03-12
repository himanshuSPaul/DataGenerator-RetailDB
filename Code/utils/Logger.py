from pathlib import Path
from datetime import datetime
import os, sys, io

RUNID = datetime.now().strftime("%Y%m%d%H%M%S")
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # Moves two levels up to the project root
LOG_PATH = PROJECT_ROOT / "logs" 
LOG_FILE_PATH = LOG_PATH / f"{(str(RUNID))}.log"



class Logger:
    def __init__(self):
       self.log_dir_path = LOG_PATH
       self.log_file_path = LOG_FILE_PATH
       self.log_file_handler = self.create_log_file()
       

    def check_if_log_dir_exist(self):
        """ Check if the directory exists, if not, create it"""
        try:

            if not self.log_dir_path.exists():
                self.log_dir_path.mkdir(parents=True, exist_ok=True)
                print(f"Created Log directory: {self.log_dir_path}")
            else:
                print(f"Directory already exists: {self.log_dir_path}")
            return True

        except PermissionError:
            print(f"Permission Denied: Cannot create directory {self.log_dir_path}. Run with proper permissions.")
        except OSError as e:
            print(f"OS Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        return None
    
    def create_log_file(self):
        if self.check_if_log_dir_exist():
            log_file_handler = open(self.log_file_path,'w')
            return log_file_handler 
        else:
            print("Failed To Create Lof File. . .")
            print("Terminating Execution...")
            sys.exit(-1)

    def log_msg(self,mesg,level='INFO',show_on_console=1):
        cur_ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        message =  f"{cur_ts} :-: {level:^8} :-: {mesg}"    #f"[{cur_ts}] [{level}] {mesg}"
        if show_on_console ==1 :
            print(message)
        if isinstance(self.log_file_handler,io.IOBase):
            self.log_file_handler.write(message)
            self.log_file_handler.flush()
            os.fsync(self.log_file_handler.fileno())








if __name__=="__main__":
    l = Logger()
    l.log_msg("Say Hello To Logger","INFO")
    l.log_msg("Say Hello To Logger","DEBUG")
    l.log_msg("Say Hello To Logger","WARNING")
    l.log_msg("Say Hello To Logger","ERROR")





# print("RUNID :",RUNID)
# print("PROJECT_ROOT :",PROJECT_ROOT)
# print("LOG_PATH :",LOG_PATH)
# print("LOG_FILE_PATH :",LOG_FILE_PATH)

# # Construct the path to the database.ini file dynamically
# CONFIG_PATH = PROJECT_ROOT / "config" / "config.ini"
   

# class Logger:
     