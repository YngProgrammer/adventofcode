from __future__ import annotations
from typing import Optional
from dataclasses import dataclass, field
import re


@dataclass
class Directory:
    name: Optional[str] = None
    parent: Optional[Directory] = None
    subdirectories: list[Directory] = field(default_factory=list)
    files: list[File] = field(default_factory=list)

    @property
    def calculated_size(self) -> int:
        total = sum(f.size for f in self.files)
        for sub in self.subdirectories:
            total += sub.calculated_size
        return total

@dataclass
class File:
    name: str
    size: int

def read_all_directories(f) -> list:
    curr = Directory()
    directories = [curr]
    for line in f.read().splitlines():
        if found := re.search(r'dir ([\w_/.-]+)', line):
            name = found.group(1)
            subdirectory = Directory(name, curr)
            directories[-1].subdirectories.append(subdirectory)
        elif found := re.search(r'(\d+) ([\w.]+)', line):
            size, name = found.groups()
            directories[-1].files.append(
                File(name, int(size))
            )
        elif found := re.search(r'^\$ (\w+)( ([\w_.-/]+))?', line):
            command = found.group(1)
            if command == 'cd':
                name = found.group(3)
                if name == '..':
                    if curr.parent is not None:
                        curr = curr.parent
                else:
                    subdirectory = next((
                        sub for sub in curr.subdirectories
                        if sub.name == name
                    ), None)
                    if subdirectory is not None:
                        curr = subdirectory
                        directories.append(curr)
    return directories

def part_1(f):
    directories = read_all_directories(f)
    return sum(
        d.calculated_size for d in directories
        if d.calculated_size <= 100000
    )

def part_2(f):
    directories = read_all_directories(f)
    total_size = max(d.calculated_size for d in directories)
    return min(
        d.calculated_size for d in directories
        if 70_000_000 - total_size + d.calculated_size >= 30_000_000
    )

if __name__ == '__main__':
    filename = 'input.txt'
    for func in (part_1, part_2):
        with open(filename) as f:
            solution = func(f)
            print(solution)