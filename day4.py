from functools import cached_property
from pprint import pprint

class TextGrid:
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

    def pattern_found(self, text_pattern: str, row: int, col: int, walk_pattern: list[tuple[int, int]]) -> tuple[int, int] | None:
        current_row = row
        current_col = col
        for idx, c in enumerate(text_pattern):
            # cut-through guard
            if current_row < 0 or current_row >= self.dim[0] or current_col < 0 or current_col >= self.dim[1]:
                return None
            if self.grid[current_row][current_col] != c:
                return None
            if idx != len(text_pattern) - 1:
                current_row += walk_pattern[idx][0]
                current_col += walk_pattern[idx][1]
        return current_row, current_col

    def find_linear_pattern(self, pattern: str):
        hits = []
        dist = len(pattern) - 1
        walk_patterns = [
            [(-1, 0)] * dist,
            [(-1, 1)] * dist,
            [(0, 1)] * dist,
            [(1, 1)] * dist,
            [(1, 0)] * dist,
            [(1, -1)] * dist,
            [(0, -1)] * dist,
            [(-1, -1)] * dist,
        ]

        rows, cols = self.dim
        for r in range(rows):
            for c in range(cols):
                for v in walk_patterns:
                    pf = self.pattern_found(pattern, r, c, v)
                    if pf is not None:
                        hits.append(((r, c), pf))
        return hits

    def find_x_pattern(self, pattern: str):
        hits = []
        new_pat = pattern * 2
        walk_patterns = [
            [(1, 1), (1, 1), (1, 1), (0, -2), (-1, 1), (-1, 1)],
            [(1, 1), (1, 1), (1, 1), (0, -2), (-1, 1), (-1, 1)],
            [(1, 1), (1, 1), (1, 1), (0, -2), (-1, 1), (-1, 1)],
            [(1, 1), (1, 1), (1, 1), (0, -2), (-1, 1), (-1, 1)],
        ]

if __name__ == '__main__':
    g = TextGrid('day4input.txt')
    hits = g.find_linear_pattern('XMAS')
    pprint(hits)
    pprint(len(hits))

