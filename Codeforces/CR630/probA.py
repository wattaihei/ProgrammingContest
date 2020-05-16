import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    Query.append((a, b, c, d, x, y, x1, y1, x2, y2))

for a, b, c, d, x, y, x1, y1, x2, y2 in Query:
    lx = x + b - a
    ly = y + d - c
    ok = False
    if (x1 <= lx <= x2 and y1 <= ly <= y2):
        if (lx == x1 == x2 and a > 0) or (ly == y1 == y2 and d > 0):
            ok = False
        else:
            ok = True
    print("Yes" if ok else "No")