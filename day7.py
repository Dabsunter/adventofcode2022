class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = {}

    @property
    def size(self):
        return sum(c.size for c in self.children.values())

    def register(self, node):
        self.children[node.name] = node

def parse_shell(input: str):
    root = Dir('root', None)
    cwd = root
    in_ls = False

    for line in input.splitlines():
        match line.split():
            case ['$', 'cd', dirname]:
                in_ls = False
                match dirname:
                    case '/':
                        while parent := cwd.parent:
                            cwd = parent
                    case '..':
                        cwd = cwd.parent
                    case _:
                        cwd = cwd.children[dirname]
                        assert isinstance(cwd, Dir)

            case ['$', 'ls']:
                in_ls = True

            case ['dir', dirname]:
                assert in_ls
                cwd.register(Dir(dirname, cwd))

            case [size, filename]:
                assert in_ls and size.isdecimal()
                cwd.register(File(filename, int(size)))

    return root

def walk_dir(dir: Dir):
    yield dir

    for subdir in (c for c in dir.children.values() if isinstance(c, Dir)):
        for c in walk_dir(subdir):
            yield c

def part1(input: str):
    root = parse_shell(input)
    return sum(c.size for c in walk_dir(root) if c.size <= 100000)

FS_CAPACITY = 70000000
NEEDED_SPACE = 30000000

def part2(input: str):
    root = parse_shell(input)
    used_space = root.size
    print("used space:", used_space)
    to_be_freed = used_space + NEEDED_SPACE - FS_CAPACITY
    print("to be freed:", to_be_freed)
    return min(c.size for c in walk_dir(root) if c.size >= to_be_freed)
