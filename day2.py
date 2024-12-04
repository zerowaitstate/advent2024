def compare(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0

class ReportStateMachine:
    def __init__(self):
        self.trend = None
        self.prior = None
        self.max_deviation = 3

    def is_safe(self, level):
        if self.trend is None and self.prior is None:
            self.prior = level
            return True
        new_trend = compare(self.prior, level)
        if new_trend == 0:
            return False
        if self.trend is None:
            self.trend = new_trend
        if abs(level - self.prior) > self.max_deviation:
            return False
        if new_trend != self.trend:
            return False
        self.prior = level
        return True


def report_is_safe(report, bad_levels):
    m = ReportStateMachine()
    bads = 0
    for x in report:
        if not m.is_safe(x):
            bads += 1
            if bads > bad_levels:
                return False
    return True

def scan_file(filename, bad_levels):
    safes = 0
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            report = [int(x) for x in line.split()]
            if report_is_safe(report, bad_levels) or (bad_levels > 0 and report_is_safe(report[1:], bad_levels-1)):
                safes += 1
    return safes


if __name__ == '__main__':
    print('part1:', scan_file('day2input.txt', 0))
    print('part2:', scan_file('day2input.txt', 1))
