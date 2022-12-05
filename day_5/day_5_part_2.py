#!/usr/bin/python3

# Advent of Code Day 5 Part 2
# https://adventofcode.com/2022/day/5#part2

def move_crates(move_count, from_stack, to_stack):
    # we change this function to incorporate the new moving ability of the crane
    crates = []

    # first we create a temp list of crates being moved
    for x in range(0, move_count):
        crates.append(from_stack.pop())

    # reverse this temp list to preserve order
    crates.reverse()

    # add this temp list of crates to the destination
    for crate in crates:
        to_stack.append(crate)

def main():
    # initialize stacks
    stack1 = ['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M']
    stack2 = ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H']
    stack3 = ['W', 'R', 'C', 'D', 'G']
    stack4 = ['N', 'B', 'S']
    stack5 = ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N']
    stack6 = ['P', 'R', 'M', 'W']
    stack7 = ['R', 'T', 'N', 'G', 'L', 'S', 'W']
    stack8 = ['Q', 'T', 'H', 'F', 'N', 'B', 'V']
    stack9 = ['L', 'M', 'H', 'Z', 'N', 'F']
    stacks = [stack1, stack2, stack3,
              stack4, stack5, stack6, 
              stack7, stack8, stack9]

    # dump file into list so we can skip the table
    file = open('input_day_5.txt', 'r')
    file_content = file.readlines()
    file.close()

    # start to iterate through lines after the table
    for i in range(10, len(file_content)):
        # split out each line so we can capture the numbers
        line_array = file_content[i].strip().split(" ")
        move_count = int(line_array[1])
        move_from = int(line_array[3])
        move_to = int(line_array[5])

        # grab the stacks to operate with
        from_stack = stacks[move_from - 1]
        to_stack = stacks[move_to - 1]

        move_crates(move_count, from_stack, to_stack)

    # once moving is done, grab the top item from each stack
    top_stacks = ""

    for stack in stacks:
        top = stack.pop()
        top_stacks += top

    print("Top crate for stacks 1 through 9: " + top_stacks)

    # Answer: BQDNWJPVJ

if __name__ == "__main__":
    main()