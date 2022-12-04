import string
from collections import Counter


def read_lines(filename: str) -> list[list[int]]:
    lines = []
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines

def part_1(lines: list[str]) -> int:
    priorities = []
    for line in lines:
        first, second = line[:(len(line) // 2)], line[(len(line) // 2):]
        common = set(first).intersection(second).pop()
        priority = ''.join(
            [string.ascii_lowercase, string.ascii_uppercase]
        ).index(common) + 1
        priorities.append(priority)
    return sum(priorities)

def part_2(lines: list[str]) -> int:
    priorities = []
    groups = [
        lines[i*3:(i+1)*3]
        for i in range(len(lines) // 3)
    ]
    for first, second, third in groups:
        common = set(first).intersection(second).intersection(third).pop()
        priority = ''.join(
            [string.ascii_lowercase, string.ascii_uppercase]
        ).index(common) + 1
        priorities.append(priority)
    return sum(priorities)

if __name__ == '__main__':
    filename = 'input.txt'
    lines = read_lines(filename)
    
    for func in (part_1, part_2):
        solution = func(lines)
        print(solution)