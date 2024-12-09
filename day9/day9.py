import heapq
from pprint import pprint

class Disk:
    ST_FILE = 1
    ST_FREE = 2

    def __init__(self):
        self.blocks: list[int|None] = []
        self.free_space_heap: list[tuple[int,int]] = []

    def load_disk_map(self, filename):
        st = Disk.ST_FILE
        cur_id = 0
        cur_pos = 0
        with open(filename, 'r') as f:
            while c := f.read(1):
                if c == '':
                    break
                if '0' <= c <= '9':
                    if st == Disk.ST_FILE:
                        self.blocks += [cur_id] * int(c)
                        cur_id += 1
                        cur_pos += int(c)
                        st = Disk.ST_FREE
                    elif st == Disk.ST_FREE:
                        if int(c) != 0:
                            self.blocks += [None] * int(c)
                            heapq.heappush(self.free_space_heap, (cur_pos, int(c)))
                            cur_pos += int(c)
                        st = Disk.ST_FILE

    def defrag(self):
        consolidated_span = (len(self.blocks), 0)
        for idx in range(len(self.blocks) - 1, -1, -1):
            # print(self.display_blocks(), self.display_free())
            if len(self.free_space_heap) == 0:
                break
            if self.free_space_heap[0][0] >= idx:
                # free space has moved to the end
                break
            if self.blocks[idx] is not None:
                # find first free span
                free_span = heapq.heappop(self.free_space_heap)
                # move block to end of span and dec span length
                file_id = self.blocks[idx]
                self.blocks[free_span[0]] = file_id
                self.blocks[idx] = None
                # dec span length
                if free_span[1] >= 2:
                    heapq.heappush(self.free_space_heap, (free_span[0] + 1, free_span[1] - 1))
            consolidated_span = (idx, consolidated_span[1] + 1)
        self.free_space_heap = []
        heapq.heappush(self.free_space_heap, consolidated_span)

    def checksum(self):
        acc = 0
        for pos in range(len(self.blocks)):
            if self.blocks[pos] is not None:
                acc += self.blocks[pos] * pos
        return acc

    def display_blocks(self):
        s = ''
        for x in range(len(self.blocks)):
            if self.blocks[x] is None:
                s += '.'
            else:
                s += str(self.blocks[x] % 10)
        return s

    def display_free(self):
        s = ' '.join([f'{span[0]}->{span[1]}' for span in self.free_space_heap])
        return s

def main():
    disk = Disk()
    disk.load_disk_map('day9input.txt')
    print(disk.display_blocks(), disk.display_free())
    disk.defrag()
    print(disk.display_blocks(), disk.display_free())
    pprint(disk.checksum())

if __name__ == '__main__':
    main()