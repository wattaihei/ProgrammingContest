import sys
input = sys.stdin.readline

N = int(input())
XYC = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    for j in range(i, N):
        x1, y1, c1 = XYC[i]
        x2, y2, c2 = XYC[j]
        r = max(abs(x1-x2), abs(y1-y2))
        # r1 + r2 = r
        # r1*c1 = r2*c2 = t
        # r1*c1 = (r-r1)*c2
        # r1 = r * c2/(c1+c2)
        t = r * c1*c2/(c1+c2)
        ans = max(t, ans)
print(ans)
        