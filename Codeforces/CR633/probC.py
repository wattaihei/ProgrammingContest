import sys
input = sys.stdin.readline

INF = 10**18

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    MA = -INF
    t = 0
    for a in A:
        if a >= MA:
            MA = a
        else:
            d = MA - a
            t = max(t, d.bit_length())
    print(t)