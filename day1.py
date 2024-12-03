

def part1():
    x = []
    y = []
    with open('day1input.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            x0, y0 = line.split()
            x.append(int(x0))
            y.append(int(y0))
    x.sort()
    y.sort()
    acc = 0
    for i in range(len(x)):
        acc += abs(x[i] - y[i])
    return acc

def part2():
    x = []
    y = []
    freq = dict()
    with open('day1input.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            x0, y0 = line.split()
            x.append(int(x0))
            y.append(int(y0))
    x.sort()
    y.sort()
    for y0 in y:
        if y0 in freq:
            freq[y0] += 1
        else:
            freq[y0] = 1
    acc = 0
    for x0 in x:
        if x0 in freq:
           acc += x0 * freq[x0]
    return acc

if __name__ == '__main__':
    print(part1())
    print(part2())
