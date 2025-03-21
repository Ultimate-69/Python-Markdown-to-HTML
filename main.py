import os

path_to_file = str(input("Enter the path to your md file: "))
if (os.path.isfile(path_to_file)):
    print("reading file...")
    md_file = open(path_to_file, 'r')
    for line in md_file:
        print(line, end='')