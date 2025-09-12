# === Python Modules ===
import os
from pathlib import Path
import logging

# === Logging Configuration ===
logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s]: %(message)s:"
)

# === Project Name ===
project_name = "interviewBot"

# === List of the files required in the project ===
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
]

# === File and Directory Creation ===
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # === Directory Creation ===
    if filedir !="":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # === File Creation ===
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")