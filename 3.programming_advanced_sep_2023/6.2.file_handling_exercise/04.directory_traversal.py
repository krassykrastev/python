# Write a program that traverses a given directory for all files. Search through the first level of the directory only
# and write information about each found file in report.txt. The files should be grouped by their extension. Extensions
# should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should
# be saved in the chosen directory.

import os

files = {}
directory = "../"


def get_files(folder, level):
    if level < 0:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = element.split(".")[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)

    else:
        get_files(f, level - 1)


get_files(directory, 1)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f".{ext}\n")
        for f_name in sorted(f_names):
            output_file.write(f"- - - {f_name}\n")
