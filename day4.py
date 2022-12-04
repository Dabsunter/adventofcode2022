def get_range(range: str):
    return tuple(map(int, range.split('-')))

def yield_elf_pairs(input: str):
    for line in input.splitlines():
        yield tuple(map(get_range, line.split(',')))

def part1(input: str):
    return sum((a1 <= a2 and b2 <= b1) or (a2 <= a1 and b1 <= b2)
               for (a1,b1),(a2,b2) in yield_elf_pairs(input))

def part2(input: str):
    return sum((b1 >= a2 or b1 >= b2) and (b2 >= a1 or b2 >= b1)
               for (a1,b1),(a2,b2) in yield_elf_pairs(input))
