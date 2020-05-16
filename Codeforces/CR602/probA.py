import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    state = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, state))

for N, state in Query:
    L = -1
    R = 10**14
    for l, r in state:
        L = max(L, l)
        R = min(R, r)
    print(max(0, L-R))