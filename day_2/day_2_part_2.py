#!/usr/bin/python3

# Advent of Code Day 2 Part 2
# https://adventofcode.com/2022/day/2#part2

# nothing changes besides the scoring system with the new info from the elf
scores = {
"A X\n" : 3,
"B X\n" : 1,
"C X\n" : 2,
"A Y\n" : 4,
"B Y\n" : 5,
"C Y\n" : 6,
"A Z\n" : 8,
"B Z\n" : 9,
"C Z\n" : 7
}

sum_scores = 0
file = open('input_day_2.txt', 'r')

for line in file:
    sum_scores += scores[line]

file.close()

print("Total score: " + str(sum_scores))

# Answer: 11657