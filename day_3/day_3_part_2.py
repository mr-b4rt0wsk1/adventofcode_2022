#!/usr/bin/python3

# Advent of Code Day 3 Part 2
# https://adventofcode.com/2022/day/3#part2

priority_sum = 0

# dump file into list so we can read 3 lines at a time
file = open('input_day_3.txt', 'r')
file_content = file.readlines()
file.close()

for i in range(0, len(file_content), 3):
    # strip newline so it doesn't show up in intersection
    elf1 = file_content[i].strip()
    elf2 = file_content[i+1].strip()
    elf3 = file_content[i+2].strip()

    # find the common item between all 3 elves
    # determine its offset based on uppercase vs lowercase
    common_item = ''.join(set(elf1).intersection(elf2, elf3))
    if common_item.isupper():
        offset = 38
    else:
        offset = 96

    # compute priority and add to running total
    priority_sum += (ord(common_item) - offset)
    
print("Priority sum of all badge items: " + str(priority_sum))

# Answer: 2798