#!/usr/bin/python3

# Advent of Code Day 12 Part 1
# https://adventofcode.com/2022/day/12

def bfs_len(graph, start, end):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    parent = {}
    parent[start] = None
    path_found = False

    # perform the bfs algorithm on the graph of possible moves
    while queue:
        m = queue.pop(0)
        if m == end:
            path_found = True
            break

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                parent[neighbor] = m

    # compute the length of the shortest path if it's found otherwise return length of 1
    path = []
    if path_found:
        path.append(end)
        curr_node_parent = parent[end]
        while curr_node_parent is not None:
            path.append(curr_node_parent)
            curr_node_parent = parent[curr_node_parent]

    return(len(path) + 1)

def main():
    # create the grid from input
    file = open('input_day_12.txt', 'r')
    grid = []
    for line in file:
        grid.append(line.strip())
    file.close()

    num_rows = len(grid)
    num_cols = len(grid[0])

    # find the starting and ending coordinates
    start_pos = []
    end_pos = []
    for i in range(0, num_rows):
        if grid[i].__contains__("S"):
            start_pos.append(i)
            start_pos.append(grid[i].index("S"))
        if grid[i].__contains__("E"):
            end_pos.append(i)
            end_pos.append(grid[i].index("E"))

    # create graph of possible moves from grid
    move_graph = {}
    for row in range(0, num_rows):
        for col in range(0, num_cols):
            move_graph[(row, col)] = []
    
            # compute the height of the current position
            if (row, col) == tuple(start_pos):
                curr_height = ord("a")
            elif (row, col) == tuple(end_pos):
                curr_height = ord("z")
            else:
                curr_height = ord(grid[row][col])

            # check if up is a possible move from current position
            if row - 1 >= 0 and ord(grid[row - 1][col]) <= curr_height + 1:
                move_graph[(row, col)].append((row - 1, col))
            # check if down is a possible move from current position
            if row + 1 < num_rows and ord(grid[row + 1][col]) <= curr_height + 1:
                move_graph[(row, col)].append((row + 1, col))
            # check if left is a possible move from current position
            if col - 1 >= 0 and ord(grid[row][col - 1]) <= curr_height + 1:
                move_graph[(row, col)].append((row, col - 1))
            # check if right is a possible move from current position
            if col + 1 < num_cols and ord(grid[row][col + 1]) <= curr_height + 1:
                move_graph[(row, col)].append((row, col + 1))

    # use bfs to find the shortest path and return its length
    shortest_path_len = bfs_len(move_graph, tuple(start_pos), tuple(end_pos))

    print("Fewest number of steps to get to the location: "+ str(shortest_path_len))

    # Answer: 383

if __name__ == "__main__":
    main()
