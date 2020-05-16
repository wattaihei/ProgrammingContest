import sys
input = sys.stdin.readline

ax, ay, bx, by = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

if ax < bx:
    ax, ay, bx, by = bx, by, ax, ay

def cross(cx, cy, dx, dy):
    if cx < dx:
        cx, cy, dx, dy = dx, dy, cx, cy
    if ax == bx:
        if (ay < by) and ((ay-cy)*(cx-dx) <= (cy-dy)*(ax-cx) <= (by-cy)*(cx-dx)):
            if (cy < dy) and (0 <= (cy-dy)*(ax-cx) <= (dy-cy)*(cx-dx)):
                return True
            if (dy < cy) and ((dy-cy)*(cx-dx) <= (cy-dy)*(ax-cx) <= 0):
                return True
        if (by < ay) and ((by-cy)*(cx-dx) <= (cy-dy)*(ax-cx) <= (ay-cy)*(cx-dx)):
            if (cy < dy) and (0 <= (cy-dy)*(ax-cx) <= (dy-cy)*(cx-dx)):
                return True
            if (dy < cy) and ((dy-cy)*(cx-dx) <= (cy-dy)*(ax-cx) <= 0):
                return True
        return False       
    bb = (ax-bx)*(cy-dy) - (ay-by)*(cx-dx)
    aa = -ax*(ay-by)*(cx-dx) + cx*(ax-bx)*(cy-dy) + (cx-dx)*(ax-bx)*(ay-cy)
    if bb > 0 and (bb*bx <= aa <= bb*ax) and (bb*dx <= aa <= bb*cx):
        return True
    if bb < 0 and (bb*ax <= aa <= bb*bx) and (bb*cx <= aa <= bb*dx):
        return True
    return False

def cross2(cx, cy, dx, dy):
    s1 = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)
    s2 = (bx-ax)*(dy-ay) - (by-ay)*(dx-ax)
    if s1*s2 < 0:
        return True
    return False


XY.append(XY[0])
count = 0
for i in range(N):
    if cross(XY[i][0], XY[i][1], XY[i+1][0], XY[i+1][1]):
        count += 1
#print(count)
print(count//2+1)