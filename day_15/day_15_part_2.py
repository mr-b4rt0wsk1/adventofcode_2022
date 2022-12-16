#!/usr/bin/python3

# Advent of Code Day 15 Part 2
# https://adventofcode.com/2022/day/15#part2

from itertools import product

file = open('input_day_15.txt', 'r')

lines = {}
for line in file:
    # parse out individual coordinates
    line = line.strip().split(" ")
    sx = int(line[2][2:-1])
    sy = int(line[3][2:-1])
    bx = int(line[8][2:-1])
    by = int(line[9][2:])
    diff = abs(sx - bx) + abs(sy - by) + 1

    # had to get help for this one
    # TODO: conceptualize the math that is going on from here to the end and rewrite it how you would write it
    for endpoints, mb, norm in [
        ((sx - diff, sx), (-1, sy - diff + sx), -1),
        ((sx, sx + diff), ( 1, sy - diff - sx), -1),
        ((sx, sx + diff), (-1, sy + diff + sx),  1),
        ((sx - diff, sx), ( 1, sy + diff - sx),  1),
    ]:
        lines.setdefault(mb, {-1:[], 1:[]})[norm].append(endpoints)

slopes = {-1: [], 1:[]}
for (m, b), norms in lines.items():
    for (x1, x2), (x3, x4) in product(*norms.values()):
        o1, o2 = max(x1, x3), min(x2, x4)
        if o1 <= o2:
            slopes[m].append((b, (o1, o2)))

for (b1, (x1, x2)), (b2, (x3, x4)) in product(slopes[-1], slopes[1]):
    x = (b2 - b1) // -2
    y = x + b2
    if x1 <= x <= x2 and x3 <= x <= x4:
        print("Tuning frequency: " + str(x * 4000000 + y))