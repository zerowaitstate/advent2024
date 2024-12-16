import copy

# coordinate system is R,C 0-indexed
class Maze:
    def __init__(self, filename: str):
        self.p = []
        self.start_pos = None
        self.end_pos = None
        self.read_file(filename)

    def read_file(self, fn: str):
        cur_row = 0
        with open(fn, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                self.p.append(list(line))
                if (s_pos := line.find('S')) != -1:
                    self.start_pos = (cur_row, s_pos)
                if (e_pos := line.find('E')) != -1:
                    self.end_pos = (cur_row, e_pos)
                cur_row += 1

    def __str__(self):
        return f'Start Pos: {self.start_pos} End Pos: {self.end_pos}  ## coordinate system is (R,C) 0-indexed ##\n' + self.display()

    def display(self, breadcrumbs: dict[tuple[int,int],str] | None=None):
        if breadcrumbs is None:
            return '\n'.join([''.join(x) for x in self.p])
        else:
            p1 = copy.deepcopy(self.p)
            for coord, crumb in breadcrumbs.items():
                p1[coord[0]][coord[1]] = crumb
            return '\n'.join([''.join(x) for x in p1])


if __name__ == '__main__':
    m = Maze('test1.txt')
    bc = dict()
    bc[(12,1)] = '^'
    bc[(11,1)] = '>'
    bc[(11,2)] = '>'
    print(m.display(bc))

