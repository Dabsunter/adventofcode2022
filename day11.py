from collections import defaultdict
from typing import Dict
from tqdm import trange
import math

class Monkey:
    def __init__(self, input_itr):
        self.id = next(input_itr).split()[1][:-1]
        self.items = [int(i) for i in next(input_itr).split(': ')[1].split(', ')]
        self.operation = next(input_itr).split('= ')[1]
        self.divisible_by = int(next(input_itr).split()[3])
        self.if_true = next(input_itr).split()[5]
        self.if_false = next(input_itr).split()[5]

        self.divisible_by_lcm = None


    def inspect(self, monkeys):
        for old in self.items:
            new = eval(self.operation)
            if self.divisible_by_lcm:
                new %= self.divisible_by_lcm
            else:
                new //= 3
            monkeys[
                self.if_true if new % self.divisible_by == 0 else self.if_false
            ].items.append(new)

        self.items.clear()

def parse_monkeys(input: str, is_part2=False) -> Dict[str, Monkey]:
    input_itr = iter(input.splitlines())
    monkeys = {}

    try:
        while True:
            m = Monkey(input_itr)
            monkeys[m.id] = m
            assert next(input_itr) == ''
    except StopIteration:
        pass

    if is_part2:
        divisible_by_lcm = math.lcm(*(m.divisible_by for m in monkeys.values()))
        for m in monkeys.values():
            m.divisible_by_lcm = divisible_by_lcm

    return monkeys

def max2(iterable):
    m1 = m2 = None
    for i in iterable:
        if not m1 or i > m1:
            m2 = m1
            m1 = i
        elif not m2 or i > m2:
            m2 = i
    return m1,m2


def part1(input):
    monkeys = parse_monkeys(input)
    monkey_business = defaultdict(lambda: 0)

    for _ in range(20):
        for m in monkeys.values():
            monkey_business[m.id] += len(m.items)
            m.inspect(monkeys)

    a,b = max2(monkey_business.values())
    return a * b


def part2(input):
    monkeys = parse_monkeys(input, is_part2=True)
    monkey_business = defaultdict(lambda: 0)

    for _ in trange(10000):
        for m in monkeys.values():
            monkey_business[m.id] += len(m.items)
            m.inspect(monkeys)

    a,b = max2(monkey_business.values())
    return a * b
