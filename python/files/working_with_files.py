# Paths
''''from pathlib import Path

Path(r"files/petnames.txt")
Path("files/petnames.txt")
path = Path("files/petnames.txt")
print(path)

print(path.name)'''


#Directories
from pathlib import Path
path = Path("/Users/nathanielofosuasiedu/Downloads/Learn/Projects/learning_python/python/modules")
print(path)
paths = [p for p in path.iterdir()]
print(paths)
py_files = [p for p in path.rglob("*.py")]
print(py_files)

#Files
from pathlib import Path
import shutil
path = Path("files/petnames.txt")
path.exists
path.rename
path.read_text
path.unlink
path.write_text('')
shutil.copy("files/petnames.txt","ecommerce") #Copy files using shutil command