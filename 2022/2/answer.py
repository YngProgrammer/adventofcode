

def read_lines(filename: str) -> list[list[int]]:
    lines = []
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines

def part_1(lines: list[str]) -> int:
    wins = {
        'Y': 'A',
        'Z': 'B',
        'X': 'C'
    }

    score = 0
    for line in lines:
        opponent, me = line.split(' ')
        if wins.get(me) == opponent:
            score += 6
        elif 'ABC'.index(opponent) == 'XYZ'.index(me):
            score += 3
        score += ('XYZ'.index(me) + 1)
    return score

def part_2(lines: list[str]) -> int:
    wins = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    score = 0
    for line in lines:
        opponent, strategy = line.split(' ')
        if strategy == 'X':
            me = wins.get(opponent)
            outcome = 0
        elif strategy == 'Y':
            me = 'XYZ'['ABC'.index(opponent)]
            outcome = 3
        else:
            me = {
                'A': 'Y',
                'B': 'Z',
                'C': 'X'
            }.get(opponent)
            outcome = 6
        score += outcome
        score += ('XYZ'.index(me) + 1)
        
    return score

if __name__ == '__main__':
    filename = 'input.txt'
    lines = read_lines(filename)
    
    solution = part_1(lines)
    print(solution)

    solution = part_2(lines)
    print(solution)