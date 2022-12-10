#!/usr/bin/python3

# Advent of Code Day 4 Part 2
# https://adventofcode.com/2022/day/4#part2

pair_sum = 0

file = open('input_day_4.txt', 'r')

for line in file:
    # split out the input into the elements of each elf's assignment
    split_pairing = line.split(",")
    elf1 = split_pairing[0].split("-")
    elf2 = split_pairing[1].split("-")

    # we need them in ranges this time
    range1 = range(int(elf1[0]),int(elf1[1])+1)
    range2 = range(int(elf2[0]),int(elf2[1])+1)

    # check if there is an intersection and add to the running total
    if set(range1).intersection(range2) != set():
        pair_sum += 1

file.close()
    
print("Number of assignment pairs where one range overlaps with another: " + str(pair_sum))

# Answer: 837