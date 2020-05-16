
# crossing point of line p0-p1 and p2-p3
def Line_Line(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y):
    retx = ((p0y-p2y)*(p0x-p1x)*(p2x-p3x) - p0x*(p2x-p3x)*(p0y-p1y) + p2x*(p2y-p3y)*(p0x-p1x)) \
        / ((p2y-p3y)*(p0x-p1x)-(p2x-p3x)*(p0y-p1y))
    if p0x != p1x:
        rety = (p0y-p1y)*(retx-p0x)/(p0x-p1x) + p0y
    else:
        rety = (p2y-p3y)*(retx-p2x)/(p2x-p3x) + p2y
    return retx, rety

# line: p0-p1
# center : (cx, cy), radius: cr
def Circle_Line(p0x, p0y, p1x, p1y, cx, cy, cr):
    tan_p = (-p1y+p0y, p1x-p0x)
    nearestx, nearesty = Line_Line(p0x, p0y, p1x, p1y, cx, cy, cx+tan_p[0], cy+tan_p[1])
    distance = ((nearestx-cx)**2+(nearesty-cy)**2)**0.5
    p_e = ((p1x-p0x)/(tan_p[0]**2+tan_p[1]**2)**0.5, (p1y-p0y)/(tan_p[0]**2+tan_p[1]**2)**0.5)
    near_to_ret = (cr**2-distance**2)**0.5
    return [
        (nearestx + near_to_ret*p_e[0], nearesty + near_to_ret*p_e[1]),
        (nearestx - near_to_ret*p_e[0], nearesty - near_to_ret*p_e[1]),        
        ]


# center : (c0x, c0y), radius: c0r
def Circle_Circle(c0x, c0y, c0r, c1x, c1y, c1r):
    d = ((c0x-c1x)**2+(c0y-c1y)**2)**0.5
    if not abs(c0r-c1r) <= d <= c0r+c1r:
        return []
    mid_p = (
        ((c0r**2-c1r**2+d**2)*c1x+(c1r**2-c0r**2+d**2)*c0x)/(2*d**2),
        ((c0r**2-c1r**2+d**2)*c1y+(c1r**2-c0r**2+d**2)*c0y)/(2*d**2)
    )
    vx = c0y - c1y
    vy = c1x - c0x
    return Circle_Line(mid_p[0], mid_p[1], mid_p[0]+vx, mid_p[1]+vy, c0x, c0y, c0r)


import sys
input = sys.stdin.readline
from math import sqrt
eps = 10**(-9)

N, K = map(int, input().split())
XYC = [list(map(int, input().split())) for _ in range(N)]

l = 0
r = 10**8
while r-l > 0.00000001:
    D = (l+r)/2
    Points = []
    for i, (x0, y0, c0) in enumerate(XYC):
        Points.append((x0, y0))
        for j, (x1, y1, c1) in enumerate(XYC):
            if i >= j: continue
            for px, py in Circle_Circle(x0, y0, D/c0, x1, y1, D/c1):
                Points.append((px, py))

    ok = False
    for px, py in Points:
        count = 0
        for x, y, c in XYC:
            if c*((x-px)**2+(y-py)**2)**0.5 <= D+eps:
                count += 1
        if count >= K:
            ok = True
            break
        
    if ok:
        r = D
    else:
        l = D

print(r)