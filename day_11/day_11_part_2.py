#!/usr/bin/python3

# Advent of Code Day 11 Part 2
# https://adventofcode.com/2022/day/11#part2

import math

class Monkey:
    def __init__(self, items, operation, divisor, throw_t, throw_f):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.throw_t = throw_t
        self.throw_f = throw_f
        self.inspect_count = 0

    def compute_worry_level(self, item):
        # computes the new worry level based on the monkey's operation
        if self.operation[1] != "old":
            operator = int(self.operation[1])
        else:
            operator = item

        if self.operation[0] == "*":
            return (item * operator)
        else:
            return (item + operator)
    
    def take_turn(self, monkeys, wm_divisor):
        for item in self.items:
            # determine the new worry level based on the monkey's operation
            # use worry management divisor
            new_worry_level = self.compute_worry_level(int(item)) % wm_divisor
            # check the worry level against the monkey's test and throw to the appropriate monkey
            if new_worry_level % self.divisor == 0:
                monkeys[self.throw_t].items.append(str(new_worry_level))
            else:
                monkeys[self.throw_f].items.append(str(new_worry_level))
        # increment the monkey's inspect count
        self.inspect_count += len(self.items)
        # empty the monkeys items since they were all thrown
        self.items = []
        return monkeys

def main():
    # parse input
    file = open('input_day_11.txt', 'r')
    lines = file.readlines()
    file.close()

    # initialize monkeys
    monkeys = []

    for line in lines:
        line_array = line.strip().split(":")
        if line_array[0].__contains__("Monkey"):
            pass
        elif line_array[0].__contains__("Starting items"):
            items = line_array[1].replace(" ", "").split(",")
        elif line_array[0].__contains__("Operation"):
            operation = line_array[1].split(" ")[4:]
        elif line_array[0].__contains__("Test"):
            divisor = int(line_array[1].split(" ")[3])
        elif line_array[0].__contains__("If true"):
            throw_t = int(line_array[1].split(" ")[4:][0])
        elif line_array[0].__contains__("If false"):
            throw_f = int(line_array[1].split(" ")[4:][0])
        else:
            monkey = Monkey(items, operation, divisor, throw_t, throw_f)
            monkeys.append(monkey)

    # add the final monkey
    monkey = Monkey(items, operation, divisor, throw_t, throw_f)
    monkeys.append(monkey)

    # 10000 rounds is a lot of rounds and the worry integers will get too large to handle
    # compute the lcm of all the monkey's divisors to find the "worry management divisor"
    # at a high level, the "worry management divisor" will help keep the worry values low
    # at the same time, it will not compromise the results of the tests the monkeys run on the worry values
    wm_divisor = math.lcm(*(monkey.divisor for monkey in monkeys))
        
    # play rounds
    for i in range(0, 10000):
        for monkey in monkeys:
            monkeys = monkey.take_turn(monkeys, wm_divisor)

    # find the level of monkey business
    inspect_counts = []
    for monkey in monkeys:
        inspect_counts.append(monkey.inspect_count)
    
    inspect_counts = sorted(inspect_counts)
    inspect_counts.reverse()
    
    print("Level of monkey business: "+ str(inspect_counts[0] * inspect_counts[1]))

    # Answer: 30893109657

if __name__ == "__main__":
    main()