# Write a program that reads the path to a file and subtracts the file name and its extension
#
# Input1: C:\Internal\training-internal\Template.pptx
# Output1:
# File name: Template
# File extension: pptx
#
# Input2: C:\Projects\Data-Structures\LinkedList.cs
# Output2:
# File name: LinkedList
# File extension: cs

filename_plus_extension = input().split("\\")
filename, extension = filename_plus_extension[-1].split(".")

print(f"File name: {filename}")
print(f"File extension: {extension}")