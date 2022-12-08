#!/usr/bin/python3

# Advent of Code Day 8 Part 2
# https://adventofcode.com/2022/day/8#part2

def calc_scenic_score(row, col, grid, grid_t):
    tree_height = grid[row][col]

    # calc row to left
    left_chunk = grid[row][:col]
    left_chunk.reverse()
    left_blocking_tree = list(filter(lambda a: a >= tree_height, left_chunk))
    if left_blocking_tree != []:
        left_score = left_chunk.index(left_blocking_tree[0]) + 1
    else:
        left_score = len(left_chunk)
    
    # calc row to right
    right_chunk = grid[row][col+1:]
    right_blocking_tree = list(filter(lambda b: b >= tree_height, right_chunk))
    if right_blocking_tree != []:
        right_score = right_chunk.index(right_blocking_tree[0]) + 1
    else:
        right_score = len(right_chunk)

    # calc col to top
    top_chunk = grid_t[col][:row]
    top_chunk.reverse()
    top_blocking_tree = list(filter(lambda c: c >= tree_height, top_chunk))
    if top_blocking_tree != []:
        top_score = top_chunk.index(top_blocking_tree[0]) + 1
    else:
        top_score = len(top_chunk)
    
    # calc col to bottom
    bottom_chunk = grid_t[col][row+1:]
    bottom_blocking_tree = list(filter(lambda d: d >= tree_height, bottom_chunk))
    if bottom_blocking_tree != []:
        bottom_score = bottom_chunk.index(bottom_blocking_tree[0]) + 1
    else:
        bottom_score = len(bottom_chunk)

    return (left_score * right_score * top_score * bottom_score)

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