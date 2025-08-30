import os
import shutil
import datetime

source_directory = ""
backup_directory = ""


def backup_directory_contents(source, backup):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup, f"backup_{timestamp}")
    try:
        shutil.copytree(source, backup_path)
        print(f"Backup completed: {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")