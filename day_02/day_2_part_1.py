#!/usr/bin/python3

# Advent of Code Day 2 Part 1
# https://adventofcode.com/2022/day/2

# there are 9 possible outcomes and each one is always scored the same way
scores = {
"A X\n" : 4,
"B X\n" : 1,
"C X\n" : 7,
"A Y\n" : 8,
"B Y\n" : 5,
"C Y\n" : 2,
"A Z\n" : 3,
"B Z\n" : 9,
"C Z\n" : 6
}

sum_scores = 0
file = open('input_day_2.txt', 'r')

# iterate through each move and sum the scores
for line in file:
    sum_scores += scores[line]

file.close()

print("Total score: " + str(sum_scores))

# Answer: 10816