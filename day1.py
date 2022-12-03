def get_elfs(input: str):
    current_elf = 0
    elfs = []
    for line in input.splitlines():
        if line:
            current_elf += int(line)
        else:
            elfs.append(current_elf)
            current_elf = 0
    if current_elf:
        elfs.append(current_elf)
    return elfs

def part1(input: str):
    return max(get_elfs(input))

def part2(input: str):
    elfs = get_elfs(input)
    elfs.sort(reverse=True)
    return sum(elfs[:3])
