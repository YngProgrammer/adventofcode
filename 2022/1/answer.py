

def read_inventories(filename: str) -> list[list[int]]:
    lines = []
    with open(filename) as f:
        lines = f.read().split('\n')

    inventories, inventory = [], []
    for line in lines:
        if not line.isdigit():
            inventories.append(inventory)
            inventory = []
        else:
            inventory.append(int(line))

    return inventories

def part_1(inventories: list[list[int]]) -> int:
    return max(
        sum(calories)
        for calories in inventories
    )

def part_2(inventories: list[list[int]]) -> int:
    sums = [
        sum(calories)
        for calories in inventories
    ]
    top_3 = []
    while len(top_3) < 3:
        largest = max(sums)
        sums.remove(largest)
        top_3.append(largest)
    return sum(top_3)

if __name__ == '__main__':
    filename = 'input.txt'
    inventories = read_inventories(filename)
    
    solution = part_1(inventories)
    print(solution)

    solution = part_2(inventories)
    print(solution)