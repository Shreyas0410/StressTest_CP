import os
import glob

# List of file patterns to delete (exclude scripts like correct.py and wrong.py)
file_patterns = ["input*", "correct*", "wrong*", "dummy*"]

# Loop through each file pattern and delete only files without extensions or with numbered suffixes
for pattern in file_patterns:
    for file in glob.glob(pattern):
        # Exclude files ending with `.py` or any other scripts
        if not file.endswith(".py"):
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except OSError as e:
                print(f"Error deleting {file}: {e}")

print("Cleanup complete!")
