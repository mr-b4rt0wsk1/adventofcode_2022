#!/usr/bin/python3

# Advent of Code Day 6 Part 1
# https://adventofcode.com/2022/day/6

# grab the datastream from the file
file = open('input_day_6.txt', 'r')
datastream = file.readlines()[0]
file.close()

queue = []
count = 0

for char in datastream:
    # use a queue to keep track of the 4 most recent characters
    queue.append(char)
    count += 1

    # break the loop if we have 4 chars in queue and they are unique
    if len(set(queue)) == 4:
        break
    # remove first char in queue if we have 4 chars in queue that are not unique 
    elif len(queue) == 4:
        queue.pop(0)
    # do nothing and continue to loop if the queue is not of length 4 yet
    else:
        pass

print("Start-of-packet begins after this amount of characters: " + str(count))

# Answer: 1034