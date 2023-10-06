# Write a program that traverses a given directory for all files. Search through the first level of the directory only
# and write information about each found file in report.txt. The files should be grouped by their extension. Extensions
# should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should
# be saved in the chosen directory.

import os

files = {}
directory = "./04.directory_traversal/"

for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = element.split(".")[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)

    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split(".")[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f".{ext}\n")
        for f_name in sorted(f_names):
            output_file.write(f"- - - {f_name}\n")
