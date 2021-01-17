import sys
input = sys.stdin.buffer.readline

N = int(input())
XY = [list(map(int, input().rstrip().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1 = XY[i]
    for j in range(i+1, N):
        x2, y2 = XY[j]
        if ((x1-x2 > 0) and ((y1-y2) <= (x1-x2) and -(x1-x2) <= (y1-y2))) or ((x1-x2 < 0) and ((x1-x2) <= (y1-y2) and -(x1-x2) >= (y1-y2))) or x1 == x2:
            ans += 1
print(ans)