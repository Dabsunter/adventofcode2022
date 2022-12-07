def first_unique_chars_idx(n, noise):
    for i in range(n, len(noise)):
        if len(set(noise[i-n:i])) == n:
            return i

def part1(input: str):
    return first_unique_chars_idx(4, input)

def part2(input: str):
    return first_unique_chars_idx(14, input)
