import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for r, w in Query:
    a = "B"*w
    b = "W" + "B"*(w-1)
    print(b)
    for _ in range(r-1):
        print(a)