#!/usr/bin/python3

# Advent of Code Day 13 Part 1
# https://adventofcode.com/2022/day/13

import ast

def compare(left, right):
    for left_element, right_element in zip(left, right):
        # if both elements are ints
        if type(left_element) == int and type(right_element) == int:
            if left_element < right_element:
                return 1
            if left_element > right_element:
                return -1
        # if both elements are lists
        elif type(left_element) == list and type(right_element) == list:
            result = compare(left_element, right_element)
            if result != 0:
                return result
        # if left element is int and right element is list
        elif type(left_element) == int:
            result = compare([left_element], right_element)
            if result != 0:
                return result
        # left element list and right element is int
        else: 
            result = compare(left_element, [right_element])
            if result != 0:
                return result
    
    # proceed to compare lenghts since no differences found in the zip comparison

    # left side ran out of items (pass)
    if len(left) < len(right):
        return 1
    # right side ran out of items (fail)
    elif len(left) > len(right):
        return -1
    # left and right were equal (continue any other comparisons)
    else:
        return 0

def main():
    # create the grid from input
    file = open('input_day_13.txt', 'r')
    lines = file.readlines()
    file.close()
    
    index = 1
    sum_indices = 0
    signal_pair = []

    # iterate through the input comparing the signal pairs
    for line in lines:
        if line == '\n':
            if compare(ast.literal_eval(signal_pair[0]), ast.literal_eval(signal_pair[1])) == 1:
                sum_indices += index
            signal_pair = []
            index += 1
        else:
            signal_pair.append(line.strip())

    # make sure final pair is accounted for
    if compare(ast.literal_eval(signal_pair[0]), ast.literal_eval(signal_pair[1])) == 1:
        sum_indices += index

    print("Sum of the indices of the signal pairs in the correct order: " + str(sum_indices))

    # Answer: 5208

if __name__ == "__main__":
    main()