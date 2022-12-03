import string

def yield_rucksacks(input: str):
    for line in input.splitlines():
        mid = len(line) // 2
        yield line[:mid], line[mid:]

def get_priority(item):
    return string.ascii_letters.index(item) + 1

def get_common_letter(compartments):
    for letter in compartments[0]:
        if all(letter in c for c in compartments[1:]):
            return letter

def part1(input: str):
    return sum(get_priority(get_common_letter(rucksack))
               for rucksack in yield_rucksacks(input))

def yield_rucksacks_by_3(input: str):
    itr = iter(input.splitlines())
    try:
        while True:
            yield next(itr), next(itr), next(itr)
    except StopIteration:
        pass

def part2(input: str):
    return sum(get_priority(get_common_letter(rucksacks))
               for rucksacks in yield_rucksacks_by_3(input))
