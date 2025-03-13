from pathlib import Path
from datetime import datetime
import os, sys, io
import logging


RUNID = datetime.now().strftime("%Y%m%d%H%M%S")
PROJECT_ROOT = Path(__file__).resolve().parent.parent  # Moves two levels up to the project root
LOG_PATH = PROJECT_ROOT / "logs" 
LOG_FILE_PATH = LOG_PATH / f"{(str(RUNID))}.log"



class Logger:
    """Singleton Logger with proper instance variable initialization."""
    
    _instance = None  # Class variable to store the single instance
    _run_id = datetime.now().strftime("%Y%m%d%H%M%S")  # Unique log file name
    _project_root = Path(__file__).resolve().parent.parent
    _log_directory = _project_root / "logs"
    _log_file_path = _log_directory / f"{_run_id}.log"
    print(f"log_file_path :{_log_file_path}")

    def __new__(cls):
        """Ensure only one instance of Logger is created."""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)

            # Instance variables must be defined inside a method
            cls._instance.run_id = cls._run_id
            cls._instance.project_root = cls._project_root
            cls._instance.log_directory = cls._log_directory
            cls._instance.log_file_path = cls._log_file_path

            # Setup log directory and logger
            cls._instance._create_log_directory()
            cls._instance._initialize_logger()

        return cls._instance

    def _create_log_directory(self):
        """Ensure the log directory exists."""
        if not self.log_directory.exists():
            self.log_directory.mkdir(parents=True, exist_ok=True)
            print(f"Created log directory: {self.log_directory}")

    def _initialize_logger(self):
        """Initialize the logger instance."""
        log_format =  "%(asctime)s | %(levelname)-6s | %(module)s:%(lineno)d | %(message)s"
        self.logger = logging.getLogger("RetailDBLOgger")  # ✅ Defined properly
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.hasHandlers():
            """Writing Log to Log File"""
            file_handler = logging.FileHandler(self.log_file_path)
            formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            """Writing Log to Console"""
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter( "%(asctime)s | %(levelname)-8s | %(message)s")
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        """Return the logger instance."""
        return self.logger

    def write_log(self, level, message,filename=__file__):
        """Write a log message dynamically with a chosen log level."""
        level = level.upper()
        log_levels = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }

        module_name = Path(filename).name
        formatted_message = f"[{module_name}] {message}"

        if level in log_levels:
            self.logger.log( log_levels[level], formatted_message) 
        else:
            # self.logger.error(f"Invalid log level: {level}. Message: {message}")
            self.logger.error(f"Invalid log level: {level}. Message: {formatted_message}")

# Example Usage
if __name__ == "__main__":
    # logger_instance = Logger().get_logger()
    # logger_instance.info("Logger initialized successfully.")

    log_instance = Logger()
    log_instance.write_log("info", "This is a test info log message.")
    log_instance.write_log("error", "This is a test error log message.")




# class Logger :
#     _instance = None 

#     def __new__(cls):
#         """Ensure only one instance of Logger is created."""
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#             cls._instance._ensure_log_directory()
#             cls._instance._setup_logger()
#         return cls._instance
    
    # def _ensure_log_directory(self):
    #     """Ensure the log directory exists."""
    #     if not self.LOG_PATH.exists():
    #         self.LOG_PATH.mkdir(parents=True, exist_ok=True)
    #         print(f"✅ Created log directory: {self.LOG_PATH}")

    # def _setup_logger(self):
    #     """Initialize the logger and set up the file handler."""
    #     self.logger = logging.getLogger("AppLogger")
    #     self.logger.setLevel(logging.DEBUG)

    #     # Prevent duplicate handlers
    #     if not self.logger.hasHandlers():
    #         file_handler = logging.FileHandler(self.LOG_FILE_PATH)
    #         file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    #         self.logger.addHandler(file_handler)


    def get_logger(self):
        """Return the logger instance."""
        return self.logger


if __name__ == "__main__":
    # logger = Logger().get_logger()
    # logger.info("Logger initialized successfully.")

    log_instance = Logger()
    log_instance.write_log("info", "This is a test info log message.")
    log_instance.write_log("error", "This is a test error log message.")


















# class Logger:
#     def __init__(self):
#        self.log_dir_path = LOG_PATH
#        self.log_file_path = LOG_FILE_PATH
#        self.log_file_handler = self.create_log_file()
       

#     def check_if_log_dir_exist(self):
#         """ Check if the directory exists, if not, create it"""
#         try:

#             if not self.log_dir_path.exists():
#                 self.log_dir_path.mkdir(parents=True, exist_ok=True)
#                 print(f"Created Log directory: {self.log_dir_path}")
#             else:
#                 print(f"Directory already exists: {self.log_dir_path}")
#             return True

#         except PermissionError:
#             print(f"Permission Denied: Cannot create directory {self.log_dir_path}. Run with proper permissions.")
#         except OSError as e:
#             print(f"OS Error: {e}")
#         except Exception as e:
#             print(f"Unexpected Error: {e}")
#         return None
    
#     def create_log_file(self):
#         if self.check_if_log_dir_exist():
#             log_file_handler = open(self.log_file_path,'w')
#             return log_file_handler 
#         else:
#             print("Failed To Create Lof File. . .")
#             print("Terminating Execution...")
#             sys.exit(-1)

#     def log_msg(self,mesg,level='INFO',show_on_console=1):
#         cur_ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#         message =  f"{cur_ts} :-: {level:^8} :-: {mesg}"    #f"[{cur_ts}] [{level}] {mesg}"
#         if show_on_console ==1 :
#             print(message)
#         if isinstance(self.log_file_handler,io.IOBase):
#             self.log_file_handler.write(message)
#             self.log_file_handler.flush()
#             os.fsync(self.log_file_handler.fileno())








# if __name__=="__main__":
#     l = Logger()
#     l.log_msg("Say Hello To Logger","INFO")
#     l.log_msg("Say Hello To Logger","DEBUG")
#     l.log_msg("Say Hello To Logger","WARNING")
#     l.log_msg("Say Hello To Logger","ERROR")





# print("RUNID :",RUNID)
# print("PROJECT_ROOT :",PROJECT_ROOT)
# print("LOG_PATH :",LOG_PATH)
# print("LOG_FILE_PATH :",LOG_FILE_PATH)

# # Construct the path to the database.ini file dynamically
# CONFIG_PATH = PROJECT_ROOT / "config" / "config.ini"
   

# class Logger:
     