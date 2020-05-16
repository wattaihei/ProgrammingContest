import sys
input = sys.stdin.readline
import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

Theta = [[0, 0] for _ in range(N)]

line = True
for i in range(N-1):
    x1, y1 = XY[i]
    for j in range(i+1, N):
        x2, y2 = XY[j]
        for k in range(N):
            x3, y3 = XY[k]
            if (y1-y2)*(x1-x3) != (y1-y3)*(x1-x2):
                line = False
                break
    if line:
        break

if line:
    for i, (x1, y1) in enumerate(XY):
        max_x = True
        min_x = True
        max_y = True
        min_y = True
        for j, (x2, y2) in enumerate(XY):
            if i == j: continue
            if x1 <= x2:
                max_x = False
            if x2 <= x1:
                min_x = False
            if y1 <= y2:
                max_y = False
            if y2 <= y1:
                min_y = False
        if max_x or min_x or max_y or min_y:
            Theta[i][1] = math.pi
else:
    for i in range(N-1):
        x1, y1 = XY[i]
        for j in range(i+1, N):
            x2, y2 = XY[j]
            if x1 == x2:
                all_right = True
                all_left = True
                for k in range(N):
                    if k == i or k == j: continue
                    x3, y3 = XY[k]
                    if x3 > x1:
                        all_left = False
                    elif x3 < x1:
                        all_right = False
                if all_right:
                    if y1 > y2:
                        Theta[i][1] = math.pi
                        Theta[j][0] = math.pi
                    elif y1 < y2:
                        Theta[i][0] = math.pi
                        Theta[j][1] = math.pi
            else:
                all_up = True
                all_down = True
                for k in range(N):
                    if k == i or k == j: continue
                    x3, y3 = XY[k]
                    if (y3-y1)*(x1-x2) < (y1-y2)*(x3-x1):
                        if x1-x2 > 0:
                            all_up = False
                        elif x1-x2 < 0:
                            all_down = False
                    elif (y3-y1)*(x1-x2) > (y1-y2)*(x3-x1):
                        if x1-x2 > 0:
                            all_down = False
                        elif x1-x2 < 0:
                            all_up = False
                if all_down:
                    if x1 < x2:
                        theta = math.atan2(x2-x1, y1-y2)
                        Theta[i][0] = theta
                        Theta[j][1] = theta
                    else:
                        theta = math.atan2(x1-x2, y2-y1)
                        Theta[i][1] = theta
                        Theta[j][0] = theta
                if all_up:
                    if x1 < x2:
                        theta = math.atan2(x1-x2, y2-y1)
                        Theta[i][1] = theta
                        Theta[j][0] = theta
                    else:
                        theta = math.atan2(x2-x1, y1-y2)
                        Theta[i][0] = theta
                        Theta[j][1] = theta

for start, end in Theta:
    delta = end - start
    while delta < 0:
        delta += 2*math.pi
    while delta >= 2*math.pi:
        delta -= 2*math.pi
    print(delta/(2*math.pi))