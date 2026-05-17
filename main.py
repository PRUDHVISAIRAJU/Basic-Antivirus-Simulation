import os
import shutil
from datetime import datetime

folder_path = "test_files"
quarantine_folder = "quarantine"

suspicious_extensions = [".exe", ".bat", ".vbs"]

log_file = "scan_log.txt"

suspicious_count = 0
total_files = 0

print("=" * 50)
print(" BASIC ANTIVIRUS SIMULATION ")
print("=" * 50)

files = os.listdir(folder_path)

with open(log_file, "a") as log:

    start_time = datetime.now()

    log.write(f"\n=== Scan Started: {start_time} ===\n")

    for file in files:

        total_files += 1

        print(f"\nChecking file: {file}")
        log.write(f"Checking file: {file}\n")

        file_path = os.path.join(folder_path, file)

        for ext in suspicious_extensions:

            if file.endswith(ext):

                suspicious_count += 1

                warning_message = f"WARNING: Suspicious file detected -> {file}"

                print(warning_message)
                log.write(warning_message + "\n")

                destination = os.path.join(quarantine_folder, file)

                shutil.move(file_path, destination)

                moved_message = f"{file} moved to quarantine."

                print(moved_message)
                log.write(moved_message + "\n")

    end_time = datetime.now()

    summary = f"""
==============================
SCAN SUMMARY
==============================
Total Files Scanned: {total_files}
Suspicious Files Found: {suspicious_count}
Scan Completed At: {end_time}
==============================
"""

    print(summary)

    log.write(summary)