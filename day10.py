def tokenize_program(input: str):
    for line in input.splitlines():
        match line.split():
            case ['addx', v]:
                yield 2, int(v)
            case ['noop']:
                yield 1, 0

def simulate_cpu(asm_tokens):
    x = 1
    for n_cycle,v in asm_tokens:
        for _ in range(n_cycle):
            yield x
        
        x += v

def part1(input: str):
    return sum(i * x
               for i,x in enumerate(simulate_cpu(tokenize_program(input)), start=1)
               if i in (20, 60, 100, 140, 180, 220))

def part2(input: str):
    screen = "vvv SCREEN vvv"
    for i,x in enumerate(simulate_cpu(tokenize_program(input))):
        i %= 40
        if i == 0:
            screen += '\n'

        if abs(i-x) <= 1:
            screen += '#'
        else:
            screen += ' '

    return screen
