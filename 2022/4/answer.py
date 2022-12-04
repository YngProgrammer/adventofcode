
def read_lines(filename: str) -> list[list[int]]:
    lines = []
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines

def part_1(lines: list[str]) -> int:
    amount = 0
    for line in lines:
        a, b = line.split(',')
        t_a, t_b = [
            tuple(map(int, v.split('-')))
            for v in (a, b)
        ]
        if any(
            t_1[0] >= t_2[0]
            and t_1[1] <= t_2[1]
            for t_1, t_2 in (
                (t_a, t_b),
                (t_b, t_a)
            )
        ):
            amount += 1
    return amount

def part_2(lines: list[str]) -> int:
    amount = 0
    for line in lines:
        a, b = [
            list(map(int, pair.split('-')))
            for pair in line.split(',')
        ]
        t_a, t_b = [
            range(s, e + 1)
            for s, e in (a, b)
        ]
        if set(t_a).intersection(t_b):
            amount += 1
    return amount

if __name__ == '__main__':
    filename = 'input.txt'
    lines = read_lines(filename)
    
    for func in (part_1, part_2):
        solution = func(lines)
        print(solution)