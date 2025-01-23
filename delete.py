#Delete all the testcases
import os
import glob

file_patterns = ["input*", "correct*", "wrong*", "dummy*"]

for pattern in file_patterns:
    for file in glob.glob(pattern):
        if not file.endswith(".py"):
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except OSError as e:
                print(f"Error deleting {file}: {e}")

print("Cleanup complete!")
