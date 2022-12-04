#!/usr/bin/python3

# Advent of Code Day 4 Part 1
# https://adventofcode.com/2022/day/4

pair_sum = 0

file = open('input_day_4.txt', 'r')

for line in file:
    # split out the input into the elements of each elf's assignment
    split_pairing = line.split(",")
    elf1 = split_pairing[0].split("-")
    elf2 = split_pairing[1].split("-")

    # check if elf1's assignment fully contains elf2's
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        pair_sum += 1
    # check if elf2's assignment fully contains elf1's
    elif int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        pair_sum += 1
    # do nothing if there is no fully contain
    else:
        pass

file.close()
    
print("Number of assignment pairs where one range fully contains another: " + str(pair_sum))

# Answer: 450