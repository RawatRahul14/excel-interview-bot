# === Pythion Modules ===
import os
import sys
import logging

# === Logging Format String ===
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# === Log Directory & File Path ===
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(
    log_dir,
    exist_ok = True
)

# === Logging Configuration ===
logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Logger")