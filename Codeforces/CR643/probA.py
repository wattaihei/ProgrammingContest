import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, K in Query:
    for _ in range(K-1):
        P = [int(n) for n in str(a)]
        b = max(P)*min(P)
        if b == 0:
            break
        a += b
    print(a)