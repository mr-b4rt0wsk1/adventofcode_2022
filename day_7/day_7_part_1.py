#!/usr/bin/python3

# Advent of Code Day 7 Part 1
# https://adventofcode.com/2022/day/7

class Directory:
    def __init__(self, name, parent_directory):
        self.name = name
        self.is_directory = True
        self.parent_directory = parent_directory
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)

    def changeDirectory(self, name):
        for child in self.children:
            if child.name == name and child.is_directory:
                return child

    def getParentDirectory(self):
        return self.parent_directory

class File:
    def __init__(self, name, size):
        self.name = name
        self.is_directory = False
        self.size = size

def getDirectorySize(directory):
    global running_sum
    # goes through and calculates sizes for directories recursively
    size = 0

    for child in directory.children:
        if child.is_directory:
            size += getDirectorySize(child) 
        else:
            size += child.size

    if size <= 100000:
        # if the directory size is at most 100000, it will add it to the running sum
        running_sum += size

    return size

# get the lines in the file, skipping the first one
file = open('input_day_7.txt', 'r')
lines = file.readlines()[1:]
file.close()

# create the directory tree structure
# start by initializing the root
root = Directory("/", None)
current_directory = root

# then go through the rest of the file creating the tree
for line in lines:
    line_array = line.strip().split(" ")
    
    if line_array[0] == "$" and line_array[1] == "cd":
        # case: cd DIRECTORY_NAME
        # action: change the directory to the given directory
        if line_array[2] != "..":
            name = line_array[2]
            current_directory = current_directory.changeDirectory(name)
        else:
        # case: cd ..
        # action: change to the parent directory
            current_directory= current_directory.getParentDirectory()

    elif line_array[0] == "$" and line_array[1] == "ls":
        # case: ls
        # action: do nothing
        pass
        
    elif line_array[0] == "dir":
        # case: new directory found
        # action: add the directory to our structure
        name = line_array[1]
        new_directory = Directory(name, current_directory)
        current_directory.addNode(new_directory)

    else:
        # case: new file found
        # action: add the file to our structure
        name = line_array[1]
        size = line_array[0]
        new_file = File(name, int(size))
        current_directory.addNode(new_file)

# go through tree and compute directory sizes to find the answer
running_sum = 0
getDirectorySize(root)
print("Total size of directories with size at most 100000: " + str(running_sum))

# Answer: 1350966