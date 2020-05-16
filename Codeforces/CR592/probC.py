import sys
input = sys.stdin.readline

n, p, w, d = map(int, input().split())

ans = []
for y in range(w+1):
    t = p - d*y
    if t >= 0 and t%w == 0:
        x = t//w
        if x+y <= n:
            ans = [x, y, n-(x+y)]
if not ans:
    print(-1)
else:
    print(*ans)