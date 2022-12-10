#!/usr/bin/python3

# Advent of Code Day 10 Part 1
# https://adventofcode.com/2022/day/10

def check_and_increment(cycles, signal_strength_sum, reg_X):
    # increments the cycle count and computes signal strength for cycles 20, 60, 100, 140, 180, and 220
    cycles += 1

    if cycles == 20 or cycles % 40 == 20:
            signal_strength = cycles * reg_X
            signal_strength_sum += signal_strength

    return cycles, signal_strength_sum

def main():
    # grab instructions from input file
    file = open('input_day_10.txt', 'r')
    lines = file.readlines()
    file.close()
    
    cycles = 0
    reg_X = 1
    signal_strength_sum = 0

    # iterate through the instructions
    for line in lines:
        if line.strip() == "noop":
            # perform noop
            cycles, signal_strength_sum = check_and_increment(cycles, signal_strength_sum, reg_X)
        else:
            # perform addx NUM
            value = int(line.strip().split(" ")[1])
            for i in range(0, 2):
                cycles, signal_strength_sum = check_and_increment(cycles, signal_strength_sum, reg_X)
            reg_X += value

    print("Sum of the six signal strengths: " + str(signal_strength_sum))

    # Answer: 15120

if __name__ == "__main__":
    main()