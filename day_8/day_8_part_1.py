#!/usr/bin/python3

# Advent of Code Day 8 Part 1
# https://adventofcode.com/2022/day/8

def is_visible(row, col, grid, grid_t):
    tree_height = int(grid[row][col])

    # check if visible in row
    if int(max(grid[row][:col])) < tree_height or int(max(grid[row][col+1:])) < tree_height:
        return True
    # check if visible in column
    elif int(max(grid_t[col][:row])) < tree_height or int(max(grid_t[col][row+1:])) < tree_height:
        return True
    else:
        return False

def main():

    # initialize the grid
    grid = []
    file = open('input_day_8.txt', 'r')

    for line in file:
        row = list(line.strip())
        grid.append(row)

    file.close()

    num_rows = len(grid)
    num_cols = len(grid[0])
    visible_trees = 0
    # store transposed matrix for easy column checking
    grid_t = list(map(list, zip(*grid)))

    # go through the inner trees and determine the amount visible
    for row in range(1, num_rows-1):
        for col in range(1, num_cols-1):
            if is_visible(row, col, grid, grid_t):
                visible_trees += 1

    # add the outermost trees to the sum since they are visible
    num_outer_trees = (num_rows + num_cols) * 2 - 4
    visible_trees += num_outer_trees
    print("Number of visible trees: " + str(visible_trees))

    # Answer: 1787

if __name__ == "__main__":
    main()