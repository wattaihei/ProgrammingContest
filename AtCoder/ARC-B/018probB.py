import sys
input = sys.stdin.readline

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(i, N-1):
        for k in range(j, N):
            x0, y0 = XY[i]
            x1, y1 = XY[j]
            x2, y2 = XY[k]
            x1 -= x0
            y1 -= y0
            x2 -= x0
            y2 -= y0
            S2 = abs(x1*y2-x2*y1)
            if S2 > 0 and S2 % 2 == 0:
                ans += 1
print(ans)
