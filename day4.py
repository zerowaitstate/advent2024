from functools import cached_property
from pprint import pprint

class TextGrid:
    scan_vector = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]

    def __init__(self, filename):
        self.grid = []
        with open(filename) as f:
            for line in f.readlines():
                self.grid.append(list(line.strip()))

    @cached_property
    def dim(self) -> tuple[int, int]:
        r = len(self.grid)
        c = len(self.grid[0])
        return r, c

    def pattern_found(self, pattern: str, row: int, col: int, step: tuple[int, int]) -> bool:
        current_row = row
        current_col = col
        for c in pattern:
            # cut-through guard
            if current_row < 0 or current_row >= self.dim[0] or current_col < 0 or current_col >= self.dim[1]:
                return False
            if self.grid[current_row][current_col] != c:
                return False
            current_row += step[0]
            current_col += step[1]
        return True

    def find_pattern(self, pattern: str):
        hits = []

        rows, cols = self.dim
        for r in range(rows):
            for c in range(cols):
                for v in self.scan_vector:
                    if self.pattern_found(pattern, r, c, v):
                        hits.append(((r, c), (r+v[0]*len(pattern),c+v[1]*len(pattern))))
        return hits

if __name__ == '__main__':
    g = TextGrid('day4input.txt')
    hits = g.find_pattern('XMAS')
    pprint(hits)
    pprint(len(hits))

