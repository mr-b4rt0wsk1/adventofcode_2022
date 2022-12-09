#!/usr/bin/python3

# Advent of Code Day 9 Part 2
# https://adventofcode.com/2022/day/9#part2

def move_head(knots, direction):
    # computes the new coordinates of the head after a single postition move
    switch = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    operand = switch.get(direction)
    knots[0][0] += operand[0]
    knots[0][1] += operand[1]

    return knots
    
def move_knot(previous_knot, current_knot):
    # moves knot based on difference in previous knot and current knot coordinates
    x_diff = previous_knot[0] - current_knot[0]
    y_diff = previous_knot[1] - current_knot[1]

    if x_diff > 0:
        current_knot[0] += 1
    elif x_diff < 0:
        current_knot[0] -= 1
    else:
        pass

    if y_diff > 0:
        current_knot[1] += 1
    elif y_diff < 0:
        current_knot[1] -= 1
    else:
        pass

    return current_knot

def not_touching(previous_knot, current_knot):
    # checks to see if the knots are touching
    if current_knot[0] in range(previous_knot[0]-1, previous_knot[0]+2) and current_knot[1] in range(previous_knot[1]-1, previous_knot[1]+2):
        return False
    else:
        return True

def perform_instruction(instruction, knots, grid):
    direction = instruction[0]
    spaces = int(instruction[1])
    for i in range(0, spaces):
        # first move the head
        knots = move_head(knots, direction)
        # move remaining knots if needed
        for j in range(1, len(knots)):
            previous_knot = knots[j-1]
            current_knot = knots[j]

            # checks if the previous knot and current knot are touching
            if not_touching(previous_knot, current_knot):
                current_knot = move_knot(previous_knot, current_knot)
                if j == len(knots)-1:
                    # check if position has been visited by the tail
                    if grid[current_knot[0]][current_knot[1]] != "#":
                        grid[current_knot[0]][current_knot[1]] = "#"

                knots[j] = current_knot
            else:
                # if at any point in the chain knots are found to be touching, break because all remaining knots are already touching
                break

    return knots, grid

def main():
    # grab the directions from the input file
    file = open('input_day_9.txt', 'r')
    lines = file.readlines()
    file.close()

    # initialize 1000x1000 grid and H & T position somewhere in the middle
    grid = [["."]*1000 for x in range(1000)]
    grid[500][500] = "#"
    knots = [[500]*2 for y in range(10)]

    for line in lines:
        instruction = line.strip().split(" ")
        knots, grid = perform_instruction(instruction, knots, grid)

    # calculate the number of positions visited by the tail
    visited = 0
    for row in grid:
        visited += row.count("#")

    print("Number of visited spaces by tail of rope: " + str(visited))

    # Answer: 2562

if __name__ == "__main__":
    main()