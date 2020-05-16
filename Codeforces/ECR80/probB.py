import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b in Query:
    n = 0
    while True:
        if 10**(n+1)-1 > b:
            break
        n += 1
    print(a*n)