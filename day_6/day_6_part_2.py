#!/usr/bin/python3

# Advent of Code Day 6 Part 2
# https://adventofcode.com/2022/day/6#part2

# grab the datastream from the file
file = open('input_day_6.txt', 'r')
datastream = file.readlines()[0]
file.close()

queue = []
count = 0

# the only thing that changes is that we need to keep track of 14 chars instead of 4

for char in datastream:
    # use a queue to keep track of the 14 most recent characters
    queue.append(char)
    count += 1

    # break the loop if we have 14 chars in queue and they are unique
    if len(set(queue)) == 14:
        break
    # remove first char in queue if we have 14 chars in queue that are not unique 
    elif len(queue) == 14:
        queue.pop(0)
    # do nothing and continue to loop if the queue is not of length 14 yet
    else:
        pass

print("Start-of-packet begins after this amount of characters: " + str(count))

# Answer: 2472