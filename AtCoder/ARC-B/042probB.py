import sys
input = sys.stdin.readline

import math

x0, y0 = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 10**12
for i in range(N):
    x1, y1 = XY[i-1]
    x2, y2 = XY[i]
    a = y1 - y2
    b = - x1 + x2
    c = x1*y2 - x2*y1
    d = abs(a*x0+b*y0+c)/math.sqrt(a**2+b**2)
    ans = min(ans, d)

print(ans)