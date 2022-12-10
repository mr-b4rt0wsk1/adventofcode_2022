#!/usr/bin/python3

# Advent of Code Day 1 Part 1
# https://adventofcode.com/2022/day/1

file = open('input_day_1.txt', 'r')

max_calories = 0
sum_calories = 0

# iterate through the list counting the calories for each elf
for line in file:
    if line != "\n":
        sum_calories += int(line)
    else:
        # do a compare to keep track of the max amount of calories from an elf
        if sum_calories > max_calories:
            max_calories = sum_calories
        sum_calories = 0

file.close()

print("Max calories carried by an elf: " + str(max_calories))

# Answer: 72602