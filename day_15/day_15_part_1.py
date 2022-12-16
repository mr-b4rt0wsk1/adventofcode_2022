#!/usr/bin/python3

# Advent of Code Day 15 Part 1
# https://adventofcode.com/2022/day/15

def main():
    file = open('input_day_15.txt', 'r')

    x_ranges = []

    for line in file:
        # parse out individual coordinates
        line = line.strip().split(" ")
        sx = int(line[2][2:-1])
        sy = int(line[3][2:-1])
        bx = int(line[8][2:-1])
        by = int(line[9][2:])

        # calculate manhattan distance between sensor and beacon, then subtract the distance between sensor and line y=2000000
        diff = abs(sx - bx) + abs(sy - by) - abs(sy - 2000000)

        # a non-negative value means that the line y=2000000 intersects with the sensor's range
        if diff >= 0: 
            # the intersection is a range from (sx - diff, 2000000) to (sx + diff, 2000000)
            x_ranges.append((sx - diff, sx + diff))

    file.close()

    not_possible = set()

    for start, end in x_ranges:
        for x in range(start, end):
            not_possible.add(x)

    print("Number of positions that cannot contain a beacon in y=2000000: " + str(len(not_possible)))

    # Answer: 5127797

if __name__ == "__main__":
    main()