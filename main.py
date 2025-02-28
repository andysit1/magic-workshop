

import os
from site import makepath
import re
from typing import List


# finds  class in object
def get_line_position(class_name):

    start_idx = None
    end_idx = None

    with open("./workshop.py", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith(f"class {class_name}"):  # Detect class start
            start_idx = i
        elif start_idx is not None and line.strip() == "":  # Blank line signals end
            end_idx = i
            break

    if start_idx is not None:
        end_idx = end_idx if end_idx is not None else len(lines)  # End at EOF if needed
        return start_idx, end_idx
    else:
        return None, None  # Class not found

def move_code_segment(dest, start, end):
    # Read source file line by line
    with open("./workshop.py", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Extract the code segment
    class_code = "".join(lines[start:end]).strip() + "\n"

    # Append to the destination file
    with open(dest, "a", encoding="utf-8") as f:
        f.write(class_code)

    # Remove the segment from the original file
    new_content = lines[:start] + lines[end:]

    with open("./workshop.py", "w", encoding="utf-8") as f:
        f.writelines(new_content)

    print(f"Moved segment {start}:{end} from workshop.py -> {dest}")

def get_classes():
    """Return a dictionary of {filepath: content}."""
    files = {}

    for root, _, filenames in os.walk("."):
        for filename in filenames:
            if filename == "workshop.py":
                path = os.path.join(root, filename)
                with open(path, "r") as f:
                    files[path] = f.read()

    # fix this area cause it's only one file i can even access
    for file, content in files.items():
        classes = re.findall(r"class (\w+)", content)
        return classes

def get_title_names(title:  str):
    p = []
    for i, letter in enumerate(title):
        if letter.isupper():
            p.append(i)


    res = []
    for i in range(len(p)):
        if i == len(p) - 1:
            res.append(title[p[i]: len(title)])
        else:
            res.append(title[p[i]: p[i + 1]])

    return res


def path_to_import(path: str):
    broken = path.split("/")

def checker_existence() -> bool:
    # implment a simple letter to dict counter
    # and check the difference
    return False

if __name__ == "__main__":
    # the flow of program is
    # get classes
    # get the position of classes
    # move the classes base on Name
    #
    # next we need to work on importing..them respectively base on cacheing the locations

    print("Starting Program")
    cls = "MagicApplication"
    path = {}
    path["MagicApplication"] = "Application/Magic.py"
    path["MagicApplication"] = path["MagicApplication"].strip(".py")


    broken = path[cls].split("/")
    imports_string = f"from {broken[0]}.{broken[1]} import {cls}"
    print(imports_string)



    # classes = get_classes()
    #
    # print(classes)

    # tmp_struct = {}

    # #assume 1 layered systee

    # if classes:
    #     for cls in classes:
    #         print(f"{cls}...")

    #         l_pos = get_line_position(cls)
    #         location = get_title_names(cls)
    #         root = "./" + location[-1]
    #         file_name = location[-2]

    #         #creates the name of the file given
    #         # root location and file name (two word idenification)
    #         path = os.path.join(root)
    #         os.makedirs(path, exist_ok=True)
    #         magic_file = os.path.join(root, f"{file_name}.py")
    #         move_code_segment(magic_file, l_pos[0], l_pos[1])

    #         # setup cache for imports
