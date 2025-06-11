import math
import sys


class Charge:
    def __init__(self, x0, y0, q0):
        self._rx = x0
        self._ry = y0
        self._q = q0

    def potentialAt(self, x, y):
        COLOMB = 8.99e09
        dx = x - self._rx
        dy = y - self._ry
        r = math.sqrt(dx * dx + dy * dy)
        if r == 0.0:
            if self._q >= 0.0:
                return float('inf')
            else:
                return float('-inf')
        return COLOMB * self._q / r

    def __str__(self):
        return '%s at (%s, %s)' % (self._q, self._rx, self._ry)


def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])

    c = Charge(.51, .63, 21.3)
    print(c)
    print(c.potentialAt(x, y))
