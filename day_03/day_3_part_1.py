#!/usr/bin/python3

# Advent of Code Day 3 Part 1
# https://adventofcode.com/2022/day/3

priority_sum = 0

file = open('input_day_3.txt', 'r')

for line in file:
    # split rucksack into 2 compartments based on midpoint
    midpoint = (len(line) - 1) // 2
    compartment1 = line[:midpoint]
    compartment2 = line[midpoint:]

    # find the common item between compartments
    # determine its offset based on uppercase vs lowercase
    common_item = ''.join(set(compartment1).intersection(compartment2))
    if common_item.isupper():
        offset = 38
    else:
        offset = 96

    # compute priority and add to running total
    priority_sum += (ord(common_item) - offset)

file.close()
    
print("Priority sum of all common rucksack items: " + str(priority_sum))

# Answer: 7824