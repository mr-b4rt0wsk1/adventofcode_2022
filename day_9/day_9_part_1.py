#!/usr/bin/python3

# Advent of Code Day 9 Part 1
# https://adventofcode.com/2022/day/9

def move_head(H_pos, direction):
    # computes the new coordinates of the head after a single postition move
    switch = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    operand = switch.get(direction)
    H_pos[0] += operand[0]
    H_pos[1] += operand[1]

    return H_pos
    
def move_tail(H_pos, T_pos):
    # moves tail based on difference in head and tail coordinates
    x_diff = H_pos[0] - T_pos[0]
    y_diff = H_pos[1] - T_pos[1]

    if x_diff > 0:
        T_pos[0] += 1
    elif x_diff < 0:
        T_pos[0] -= 1
    else:
        pass

    if y_diff > 0:
        T_pos[1] += 1
    elif y_diff < 0:
        T_pos[1] -= 1
    else:
        pass

    return T_pos

def not_touching(H_pos, T_pos):
    # checks to see if the tail is not touching the head
    if T_pos[0] in range(H_pos[0]-1, H_pos[0]+2) and T_pos[1] in range(H_pos[1]-1, H_pos[1]+2):
        return False
    else:
        return True

def perform_instruction(instruction, H_pos, T_pos, grid):
    direction = instruction[0]
    spaces = int(instruction[1])
    for i in range(0, spaces):
        # first move the head
        H_pos = move_head(H_pos, direction)

        # next move the tail if it isn't touching the head
        if not_touching(H_pos, T_pos):
            T_pos = move_tail(H_pos, T_pos)

            # also need to check if the position has been visited by the tail
            if grid[T_pos[0]][T_pos[1]] != "#":
                grid[T_pos[0]][T_pos[1]] = "#"

    return H_pos, T_pos, grid

def main():
    # grab the directions from the input file
    file = open('input_day_9.txt', 'r')
    lines = file.readlines()
    file.close()

    # initialize 1000x1000 grid and H & T position somewhere in the middle
    grid = [["."]*1000 for x in range(1000)]
    grid[500][500] = "#"
    H_pos = [500, 500]
    T_pos = [500, 500]

    for line in lines:
        instruction = line.strip().split(" ")
        H_pos, T_pos, grid = perform_instruction(instruction, H_pos, T_pos, grid)

    # calculate the number of positions visited by the tail
    visited = 0
    for row in grid:
        visited += row.count("#")

    print("Number of visited spaces by tail of rope: " + str(visited))

    # Answer: 6197

if __name__ == "__main__":
    main()