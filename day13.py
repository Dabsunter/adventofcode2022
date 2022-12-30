from functools import cmp_to_key

def is_ordered(left, right):
    if not isinstance(left, list):
        left = [left]
    
    if not isinstance(right, list):
        right = [right]

    for l,r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            if (ordered := is_ordered(l, r)) is not None:
                return ordered
        elif l != r:
            return l < r

    if len(left) == len(right):
        return None

    return len(left) < len(right)

def yield_packet_pairs(input: str):
    line_itr = iter(input.splitlines())
    is_first = True
    while is_first or next(line_itr, None) is not None:
        yield eval(next(line_itr)), eval(next(line_itr))
        is_first = False

def part1(input: str):
    return sum(
        i
        for i, pair in enumerate(yield_packet_pairs(input), start=1)
        if is_ordered(*pair)
    )

def compare(a, b):
    return -1 if is_ordered(a, b) else 1

def part2(input: str):
    dividers = ([[2]], [[6]])
    packets = list(dividers)

    for pair in yield_packet_pairs(input):
        packets.extend(pair)

    packets.sort(key=cmp_to_key(compare))

    res = 1

    for i,packet in enumerate(packets, start=1):
        if packet in dividers:
            res *= i

    return res
    