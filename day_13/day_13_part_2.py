#!/usr/bin/python3

# Advent of Code Day 13 Part 2
# https://adventofcode.com/2022/day/13#part2

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

    # append all packets
    packets = []
    for line in lines:
        if line != '\n':
            packets.append(line.strip())
    packets.append("[[2]]")
    packets.append("[[6]]")

    # go through and compare all packets with each of the two decoder packets
    # if a packet is to the left of a decoder packet, add one to the decoder packet's index
    index_2 = 1
    index_6 = 1
    for packet in packets:
        if compare(ast.literal_eval(packet), [[2]]) == 1:
            index_2 += 1
        if compare(ast.literal_eval(packet), [[6]]) == 1:
            index_6 += 1

    print("Decoder key: " + str(index_2 * index_6))

    # Answer: 25792

if __name__ == "__main__":
    main()