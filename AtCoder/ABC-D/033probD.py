import numpy as np
from bisect import bisect_left

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

a1 = 0
a2 = 0
for i, (x0, y0) in enumerate(XY):
    Theta = []
    for j, (x, y) in enumerate(XY):
        if i == j: continue
        theta = np.arccos((x-x0)/((x-x0)**2+(y-y0)**2)**0.5) * 180 / np.pi
        if y < y0:
            theta = 360 - theta
        Theta += [theta, theta+360]
    Theta.sort()
    b1, b2 = 0, 0
    for theta in Theta:
        if theta >= 360: break
        il = bisect_left(Theta, theta+90)
        ir = bisect_left(Theta, theta+270)
        if abs(Theta[il]-(theta+90)) < 1E-6:
            b1 += 1
            il += 1
        if abs(Theta[ir]-(theta+270)) < 1E-6:
            b1 += 1
            ir -= 1
        b2 += ir - il
    a1 += b1//2
    a2 += b2//2


print(N*(N-1)*(N-2)//6-a1-a2, a1, a2)