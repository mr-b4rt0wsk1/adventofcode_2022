#!/usr/bin/python3

# Advent of Code Day 11 Part 1
# https://adventofcode.com/2022/day/11

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
    
    def take_turn(self, monkeys):
        for item in self.items:
            # determine the new worry level based on the monkey's operation
            # use integer division since our worry level decreases after inspection
            new_worry_level = self.compute_worry_level(int(item)) // 3
            # check the worry level against the monkey's test and throw to the appropriate monkey
            if new_worry_level % self.divisor == 0:
                monkeys[self.throw_t].items.append(str(new_worry_level))
            else:
                monkeys[self.throw_f].items.append(str(new_worry_level))
        # increment the monkey's inspect count
        self.inspect_count += len(self.items)
        # empty the monkey's items since they were all thrown
        self.items = []
        return monkeys

def main():
    # parse input into monkey objects
    file = open('input_day_11.txt', 'r')
    lines = file.readlines()
    file.close()

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
        
    # play rounds
    for i in range(0, 20):
        for monkey in monkeys:
            monkeys = monkey.take_turn(monkeys)

    # find the level of monkey business
    inspect_counts = []
    for monkey in monkeys:
        inspect_counts.append(monkey.inspect_count)
    
    inspect_counts = sorted(inspect_counts)
    inspect_counts.reverse()
    
    print("Level of monkey business: "+ str(inspect_counts[0] * inspect_counts[1]))

    # Answer: 90882

if __name__ == "__main__":
    main()