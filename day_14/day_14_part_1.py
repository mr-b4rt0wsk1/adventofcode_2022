#!/usr/bin/python3

# Advent of Code Day 14 Part 1
# https://adventofcode.com/2022/day/14

def create_rocks(data):
    all_rocks = set()

    for rock_path in data:
        for edge1, edge2 in zip(rock_path, rock_path[1:]):
            rocks = []
            # if x coordinates are equal
            if edge1[0] - edge2[0] == 0:
                # see which edge's y coordinate comes first
                if edge1[1] < edge2[1]:
                    start = edge1
                    end = edge2
                else:
                    start = edge2
                    end = edge1
                # then add the rocks in the range (column)
                for i in range(start[1], end[1] + 1):
                    rocks.append([edge1[0], i])
            # if y coordinates are equal
            else:
                # see which edge's x coordinate comes first
                if edge1[0] < edge2[0]:
                    start = edge1
                    end = edge2
                else:
                    start = edge2
                    end = edge1
                # then add the rocks in the range (row)
                for i in range(start[0], end[0] + 1):
                    rocks.append([i, edge1[1]])

            # convert the list of rocks to tuples and add as union with current set
            all_rocks.update(tuple(t) for t in rocks)

    return all_rocks

def sand_simulation(all_rocks, abyss):
    # initialize resting sand count, origin of the sand, path of the sand
    rest_counter = 0
    sand_origin = (500, 0)
    path = [sand_origin]

    while True:
        # use the previous point in path
        sand = path[-1]

        # sand attempts to move downward -> straight down, diagonally left, diagonally right (in that order)
        for diff in [0, -1, 1]:
            next_sand = (sand[0] + diff, sand[1] + 1)
            # next_sand isn't a possible move
            if next_sand in all_rocks:
                continue
            # next_sand is a possible move
            path.append(next_sand)
            break
        else:
            # if none of 3 moves are possible, inc resting sand, backtrack up path of sand and continue
            rest_counter += 1
            all_rocks.add(sand)
            path.pop()

        # stop if the sand is flowing into the abyss
        if sand[1] > abyss:
            break
    
    return rest_counter
                

def main():
    # parse the input
    data = []
    file = open('input_day_14.txt', 'r')

    for line in file:
        path = []
        for pair in line.strip().split(" -> "):
            coords = list(map(int, pair.split(",")))
            path.append(coords)
        data.append(path)

    file.close()

    # use the parsed input to create a set of rock coordinates and simulate the sand
    all_rocks = create_rocks(data)
    abyss = max(rock[1] for rock in all_rocks)
    rest_counter = sand_simulation(all_rocks, abyss)

    print("Units of sand that come to rest before flowing into the abyss: " + str(rest_counter))

    # Answer: 913

if __name__ == "__main__":
    main()