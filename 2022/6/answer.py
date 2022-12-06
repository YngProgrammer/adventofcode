
def part_1(f) -> int:
    datastream, i = f.read(), 0
    while i + 4 < len(datastream):
        marker = set(datastream[i:i+4])
        if len(marker) == 4:
            break
        i += 1
    return i + 4

def part_2(f) -> int:
    datastream, i = f.read(), 0
    while i + 4 < len(datastream):
        marker = set(datastream[i:i+4])
        if len(marker) == 4:
            break
        i += 1
    while i + 14 < len(datastream):
        marker = set(datastream[i:i+14])
        if len(marker) == 14:
            break
        i += 1
    return i + 14

if __name__ == '__main__':
    filename = 'input.txt'
    for func in (part_1, part_2):
        with open(filename) as f:
            solution = func(f)
            print(solution)