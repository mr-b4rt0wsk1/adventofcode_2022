#!/usr/bin/python3

# Advent of Code Day 8 Part 2
# https://adventofcode.com/2022/day/8#part2

def calc_scenic_score(row, col, grid, grid_t):
    tree_height = grid[row][col]
    chunks = []
    scenic_score = 1

    # a "chunk" refers to the list of trees from our current position to the outside of the grid in a certain direction (left, right, top, bottom)

    # left chunk
    chunks.append(list(reversed(grid[row][:col])))
    # right chunk
    chunks.append(grid[row][col+1:])
    # top chunk
    chunks.append(list(reversed(grid_t[col][:row])))
    # bottom chunk
    chunks.append(grid_t[col][row+1:])

    for chunk in chunks:
        blocking_tree = list(filter(lambda i: i >= tree_height, chunk))
        
        # compute the score for the chunk based on whether this is a blocking tree or not
        if blocking_tree != []:
            scenic_score *= chunk.index(blocking_tree[0]) + 1
        else:
            scenic_score *= len(chunk)

    return scenic_score

def main():
    # initialize the grid
    grid = []
    file = open('input_day_8.txt', 'r')

    for line in file:
        row = list(line.strip())
        row_ints = [eval(x) for x in row]
        grid.append(row_ints)

    file.close()

    num_rows = len(grid)
    num_cols = len(grid[0])
    scenic_scores = []
    # store transposed matrix for easy column checking
    grid_t = list(map(list, zip(*grid)))

    # go through the inner trees and determine the max scenic score
    for row in range(1, num_rows-1):
        for col in range(1, num_cols-1):
            scenic_scores.append(calc_scenic_score(row, col, grid, grid_t))

    print("Max scenic score: " + str(max(scenic_scores)))

    # Answer: 440640

if __name__ == "__main__":
    main()