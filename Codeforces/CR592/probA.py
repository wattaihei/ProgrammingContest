import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b, c, d, k in Query:
    x = (a+c-1)//c
    y = (b+d-1)//d
    if x+y <= k:
        print(x, y)
    else:
        print(-1)