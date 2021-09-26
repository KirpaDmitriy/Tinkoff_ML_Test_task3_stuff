import math


def f(x, y):
    return math.exp((x+y)/2)*((x*x-4*y*y)**3)


x0, y0 = -16, 4
x, y = x0 - 1, y0 - 1
dx, dy = 0.5, 0.5
while x <= x0 + 1:
    while y <= y0 + 1:
        print(f(x, y), end='\t')
        y += dy
    y = y0 - 1
    x += dx
    print()
