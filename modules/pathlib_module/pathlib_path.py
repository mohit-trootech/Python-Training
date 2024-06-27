from pathlib import Path
import os
from display_dir_tree import tree

#
# current_path = Path.cwd()
# print(current_path)
# print("stem", current_path.stem)
# print("name", current_path.name)
# print("suffix", current_path.suffix)
# print("parent", current_path.parent)
# print("anchor", current_path.anchor)
# print("drive", current_path.drive)
# print("parts", current_path.parts)
# print("suffixes", current_path.suffixes)
# current_file = Path(__file__)
# print(current_file)
file = Path("hello.py")
print(file.read_bytes())
eval(file.read_bytes())
print(file.exists())
print(Path.touch("New Test File 2"))
