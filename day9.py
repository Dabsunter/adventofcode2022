import math
from collections import namedtuple
from itertools import pairwise

Point = namedtuple('Point', 'x, y')

def abs_ceil(value):
    x = math.ceil(abs(value))
    return x if value >= 0 else -x

def apply_moves(moves, n_knots=2):
    knots = [Point(0, 0)] * n_knots

    explore = [{knot} for knot in knots]

    for dir,steps in moves:
        to_add = (1, 0) if dir == 'R' \
            else (0, 1) if dir == 'U' \
            else (-1,0) if dir == 'L' \
            else (0,-1) if dir == 'D' \
            else (0, 0)

        for _ in range(steps):
            knots[0] = h = Point(*map(int.__add__, knots[0], to_add))
            explore[0].add(h)

            for i in range(1, len(knots)):
                h,t = knots[i-1], knots[i]
                if max(abs(a-b) for a,b in zip(h,t)) > 1:
                    knots[i] = t = Point(*map(lambda a,b: a + abs_ceil((b-a)/2), t, h))
                    explore[i].add(t)

    return explore

def yield_moves(input: str):
    for line in input.splitlines():
        dir,steps = line.split()
        yield dir, int(steps)

def part1(input: str):
    h,t = apply_moves(yield_moves(input))
    return len(t)

def part2(input: str):
    explore = apply_moves(yield_moves(input), n_knots=10)
    return len(explore[9])
