import sys
input = sys.stdin.buffer.readline

INF = 10**18

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort()

ans = 0
x0, y0 = XY[0]
m1 =  -x0+y0# 今ままでのmax
m2 = x0+y0
for x, y in XY:
    ans = max(ans, x+m1 - y)
    ans = max(ans, y - (-x+m2))
    m1 = max(m1, -x+y)
    m2 = min(m2, x+y)
print(ans)