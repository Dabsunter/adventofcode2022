import string
from collections import deque
from itertools import product


def parse_map(input: str):
    start = None
    end = None

    def get_height(coords, c: str):
        nonlocal start, end
        if c == 'S':
            start = coords
            return get_height(coords, 'a')
        elif c == 'E':
            end = coords
            return get_height(coords, 'z')
        return string.ascii_lowercase.index(c)

    heights = [[get_height((i,j), c) for j,c in enumerate(line)] for i,line in enumerate(input.splitlines())]

    return heights, start, end


def explore(heights, start, end):
    len_x = len(heights)
    len_y = len(heights[0])

    # print('start:', start, 'end:', end, '\n', heights)

    def get_next_pos(i,j):
        if i > 0:       yield (i-1,j)
        if i < len_x-1: yield (i+1, j)
        if j > 0:       yield (i,j-1)
        if j < len_y-1: yield (i, j+1)

    def can_jump(pos1, pos2):
        i,j = pos1
        k,l = pos2
        return (heights[k][l] - heights[i][j]) <= 1

    to_explore = deque()

    to_explore.append((start, [start]))
    explored = {start}

    while to_explore:
        pos,itinerary = to_explore.popleft()

        # print('exploring', pos, 'height:', string.ascii_lowercase[heights[pos[0]][pos[1]]], 'explored:', len(explored))

        if pos == end:
            return len(itinerary) - 1

        
        for next_pos in get_next_pos(*pos):
            if next_pos not in explored and can_jump(pos, next_pos):
                to_explore.append((next_pos, itinerary + [next_pos]))
                explored.add(next_pos)

    return len_x * len_y


def part1(input: str):
    heights, start, end = parse_map(input)
    return explore(heights, start, end)


def part2(input: str):
    heights, start, end = parse_map(input)
    return min(explore(heights, pos, end)
               for pos in filter(lambda p: heights[p[0]][p[1]] == 0, product(range(len(heights)), range(len(heights[0])))))