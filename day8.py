from itertools import product

def parse_tree_map(input: str):
    tree_map = [[int(c) for c in line] for line in input.splitlines()]
    return tree_map, len(tree_map), len(tree_map[0])

def part1(input: str):
    tree_map, len_x, len_y = parse_tree_map(input)
    
    return sum(
           max((tree_map[i][y] for i in range(x)),          default=-1) < tree_map[x][y]
        or max((tree_map[i][y] for i in range(x+1, len_x)), default=-1) < tree_map[x][y]
        or max((tree_map[x][j] for j in range(y)),          default=-1) < tree_map[x][y]
        or max((tree_map[x][j] for j in range(y+1, len_y)), default=-1) < tree_map[x][y]
        for x,y in product(range(len_x), range(len_y))
    )

def count_until(iterable):
    i = 0
    for i,x in enumerate(iterable, start=1):
        if x:
            break
    return i

def part2(input: str):
    tree_map, len_x, len_y = parse_tree_map(input)
    
    return max(
          count_until(tree_map[i][y] >= tree_map[x][y] for i in reversed(range(x)))
        * count_until(tree_map[i][y] >= tree_map[x][y] for i in range(x+1, len_x))
        * count_until(tree_map[x][j] >= tree_map[x][y] for j in reversed(range(y)))
        * count_until(tree_map[x][j] >= tree_map[x][y] for j in range(y+1, len_y))
        for x,y in product(range(len_x), range(len_y))
    )
