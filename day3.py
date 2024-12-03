import re
from pprint import pprint

if __name__ == '__main__':
    with open('day3input.txt', 'r') as f:
        s = f.read(1000000)
        acc = 0
        enable = True
        for v in re.findall(r'(mul)\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', s):
            pprint(v)
            if v[0] == 'mul':
                if enable:
                    acc += int(v[1]) * int(v[2])
            elif v[3] == 'do':
                enable = True
            elif v[4] == "don't":
                enable = False
            else:
                print('error')
        print(acc)

