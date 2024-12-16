from dataclasses import dataclass, field


@dataclass
class Region():
    id: int
    letter: str
    last_offsets: set[int] = field(default_factory=set)
    perimeter: int = 0
    area: int = 0

    def price(self):
        return self.perimeter * self.area



# this function has side effects in region_db
def parse_current_line(line, last_positions, region_db):
    new_positions = []
    prev_cell_region = None
    for idx, letter in enumerate(line):
        cont_region = None
        if prev_cell_region is not None and region_db[prev_cell_region].letter == letter:
            # this is a continuation of that region
            cont_region = region_db[prev_cell_region]
        if cont_region is None and last_positions is not None and last_positions[idx].letter == letter:
            cont_region = region_db[last_positions[idx]]
        if cont_region is not None:
            cont_region.area +
        else:
            pass

        matches_previous_line = (idx < len(last_positions)) and (last_positions[idx] == letter)
        matches_previous_position = (idx > 0) and (new_positions[idx - 1] == letter)





    return new_positions

def part1():
    region_db: dict[int, Region] = {}
    last_positions = []
    with open('day12.txt') as f:
        next_id = 0
        while True:
            line = f.readline()
            if not line:
                break
            current_positions = parse_current_line(line, last_positions, region_db)
            last_positions = current_positions


if __name__ == '__main__':
    part1()