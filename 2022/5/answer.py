import re


def read_lines(filename: str) -> list[list[int]]:
    lines = []
    with open(filename) as f:
        lines = (l for l in f.read().split('\n'))
    return lines

def read_stacks(lines: str) -> str:
    stack_lines = []
    while not re.search(r'(\s+(\d+))+', line := next(lines)):
        stack_lines.append(line)
    next(lines) # XXX: move to 1st instruction line
    indexes = [i for i, c in enumerate(line) if c.isdigit()]
    return [
        [
            stack_line[i] for stack_line in stack_lines 
            if re.search(r'[A-Z]', stack_line[i])
        ]
        for i in indexes
    ]

def part_1(lines: list[str]) -> str:
    stacks = read_stacks(lines)
    for line in lines:
        amount, start, end = map(int, re.findall(r'\s(\d+)', line))
        start, end = map(lambda v: v - 1, (start, end))
        for _ in range(amount):
            stacks[end].insert(0, stacks[start].pop(0))
    return ''.join(stack[0] for stack in stacks)

def part_2(lines: list[str]) -> str:
    stacks = read_stacks(lines)
    for line in lines:
        amount, start, end = map(int, re.findall(r'\s(\d+)', line))
        start, end = map(lambda v: v - 1, (start, end))
        if amount < 2:
            stacks[end].insert(0, stacks[start].pop(0))
        else:
            for i in range(amount):
                stacks[end].insert(0, stacks[start].pop(amount - i - 1))
    return ''.join(stack[0] for stack in stacks)

if __name__ == '__main__':
    filename = 'input.txt'
    for func in (part_1, part_2):
        lines = read_lines(filename)
        solution = func(lines)
        print(solution)