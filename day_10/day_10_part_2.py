#!/usr/bin/python3

# Advent of Code Day 10 Part 2
# https://adventofcode.com/2022/day/10#part2

def draw_pixel(cycles, crt, sprite_pos):
    # draws a pixel based on if the sprite is positioned in that pixel during the cycle
    if cycles in range(sprite_pos-1, sprite_pos+2):
        crt[cycles] = "#"
    else:
        crt[cycles] = "."
    cycles += 1
    
    return cycles, crt

def main():
    # grab instructions from input file
    file = open('input_day_10.txt', 'r')
    lines = file.readlines()
    file.close()
    
    cycles = 0
    reg_X = 1
    sprite_pos = 1
    crt = [" "]*240

    # iterate through the instructions
    for line in lines:
        if line.strip() == "noop":
            # perform noop
            cycles, crt = draw_pixel(cycles, crt, sprite_pos)
            sprite_pos = reg_X + (cycles // 40 * 40)
        else:
            # perform addx NUM
            value = int(line.strip().split(" ")[1])
            for i in range(0, 2):
                cycles, crt = draw_pixel(cycles, crt, sprite_pos)
            reg_X += value
            sprite_pos = reg_X + (cycles // 40 * 40)
            
    # display the CRT
    row = []
    for pixel in range(0, len(crt)):
        if pixel != 0 and pixel % 40 == 0:
            print(''.join(row))
            row = []
        row.append(crt[pixel])
    print(''.join(row))
    
    # Answer: RKPJBPLA

if __name__ == "__main__":
    main()