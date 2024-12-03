def is_safe(report):
    trend = None
    prior = None
    for level in report:
        if prior is None:
            pass
        elif trend is None:
            trend = level - prior
            if trend == 0 or abs(level - prior) > 3:
                return False
        elif (level == prior) or abs(level - prior) > 3:
            return False
        elif (trend > 0 and level < prior) or (trend < 0 and level > prior):
            return False
        prior = level
    return True

def part1(filename):
    safes = 0
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            report = [int(x) for x in line.split()]
            if is_safe(report):
                safes += 1
            else:
                pass
    return safes


if __name__ == '__main__':
    print(part1('day2input.txt'))