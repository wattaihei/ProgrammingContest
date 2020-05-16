import sys
input = sys.stdin.readline

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1 = XY[i]
    for j in range(i+1, N):
        x2, y2 = XY[j]
        count = 0
        for x, y in XY:
            if (y1-y)*(x2-x) == (y2-y)*(x1-x):
                count += 1
        ans = max(ans, count)
print(ans)