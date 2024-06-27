from pathlib import Path
import os
from datetime import datetime

directory = Path.cwd()

print(directory)
for file in directory.iterdir():
    print(f"{file} Stat: ", datetime.fromtimestamp(os.path.getctime(file)))
