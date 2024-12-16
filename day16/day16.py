class Maze:
    def __init__(self, filename):
        self.p = []
        self.start_pos = None
        self.end_pos = None
        self.read_file(filename)

    def read_file(self, fn):
        cur_row = 0
        with open(fn, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                self.p.append(line)
                if (s_pos := line.find('S')) != -1:
                    self.start_pos = (s_pos, cur_row)
                if (e_pos := line.find('E')) != -1:
                    self.end_pos = (e_pos, cur_row)
                cur_row += 1

    def __str__(self):
        return f'Start Pos: {self.start_pos} End Pos: {self.end_pos}\n' + '\n'.join(self.p)

if __name__ == '__main__':
    m = Maze('day16.txt')
    print(m)
