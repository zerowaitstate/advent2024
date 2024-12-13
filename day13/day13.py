import re

def solve_2x2(m):
    ax = m[0][0]
    bx = m[0][1]
    x0 = m[0][2]
    ay = m[1][0]
    by = m[1][1]
    y0 = m[1][2]
    b = (y0 * ax - ay * x0) / ((by * ax) - (ay * bx))
    a = x0 / ax - (bx / ax) * b
    return a, b

def verify(m, a, b):
    ax = m[0][0]
    bx = m[0][1]
    x0 = m[0][2]
    ay = m[1][0]
    by = m[1][1]
    y0 = m[1][2]
    return ax * a + bx * b == x0 and ay * a + by * b == y0

def part1():
    a_cost = 3
    b_cost = 1
    token_acc = 0
    pat = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', re.MULTILINE)
    with open('day13.txt', 'r') as f:
        data = f.read()
        for m in re.finditer(pat, data):
            m = [[int(m.group(1)), int(m.group(3)), int(m.group(5))],
                 [int(m.group(2)), int(m.group(4)), int(m.group(6))]]
            a, b = solve_2x2(m)
            a_press = round(a)
            b_press = round(b)
            if verify(m, a_press, b_press):
                token_acc += a_press * a_cost + b_press * b_cost
    return token_acc

def part2():
    a_cost = 3
    b_cost = 1
    token_acc = 0
    pat = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', re.MULTILINE)
    with open('day13.txt', 'r') as f:
        data = f.read()
        for m in re.finditer(pat, data):
            m = [[int(m.group(1)), int(m.group(3)), int(m.group(5))+10000000000000],
                 [int(m.group(2)), int(m.group(4)), int(m.group(6))+10000000000000]]
            a, b = solve_2x2(m)
            a_press = round(a)
            b_press = round(b)
            if verify(m, a_press, b_press):
                token_acc += a_press * a_cost + b_press * b_cost
    return token_acc


if __name__ == '__main__':
    print('part1', part1())
    print('part2', part2())

