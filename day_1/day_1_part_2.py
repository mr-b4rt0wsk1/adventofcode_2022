#!/usr/bin/python3

# Advent of Code Day 1 Part 2
# https://adventofcode.com/2022/day/1#part2

file = open('input_day_1.txt', 'r')

# we now need to keep track of each sum to sort them later
sum_calories_list= []
sum_calories = 0

# for loop modified to append sums to the list
for line in file:
    if line != "\n":
        sum_calories += int(line)
    else:
        sum_calories_list.append(sum_calories)
        sum_calories = 0

file.close()

sum_calories_list.sort(reverse = True)
# take sum of the top 3
print("Sum calories carried by top 3 elves: " + str(sum(sum_calories_list[:3])))

# Answer: 207410