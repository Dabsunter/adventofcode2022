from typing import Iterator


def read_stack_state(input_itr: Iterator[str]):
    stacks = None

    def pos(i):
        return 1 + 4*i

    while (line := next(input_itr)) and line[0] == '[':
        if stacks is None:
            stacks = [[] for _ in range( (len(line)+1) // 4 )]

        for i, stack in enumerate(stacks):
            if (crate := line[pos(i)]) != ' ':
                stack.append(crate)

    for stack in stacks:
        stack.reverse()

    return {line[pos(i)]: stack for i,stack in enumerate(stacks)}

def apply_moves(stacks, input_itr: Iterator[str], mover):
    while line := next(input_itr, False):
        args = line.split()
        assert args[0] == 'move'
        n_move = int(args[1])
        assert args[2] == 'from'
        orig = args[3]
        assert args[4] == 'to'
        dest = args[5]

        mover(stacks, n_move, orig, dest)

def mover_9000(stacks, n_move, orig, dest):
    for _ in range(n_move):
            stacks[dest].append(stacks[orig].pop())


def part1(input: str):
    input_itr = iter(input.splitlines())
    stacks = read_stack_state(input_itr)
    assert next(input_itr) == ''  # Blank line
    apply_moves(stacks, input_itr, mover_9000)

    return "".join(stack[-1] for stack in stacks.values())
        

def mover_9001(stacks, n_move, orig, dest):
    stacks[dest].extend(stacks[orig][-n_move:])
    stacks[orig] = stacks[orig][:-n_move]

def part2(input: str):
    input_itr = iter(input.splitlines())
    stacks = read_stack_state(input_itr)
    assert next(input_itr) == ''  # Blank line
    apply_moves(stacks, input_itr, mover_9001)

    return "".join(stack[-1] for stack in stacks.values())

