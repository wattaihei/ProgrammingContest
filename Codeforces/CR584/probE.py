import sys
input = sys.stdin.readline
from itertools import permutations

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    state = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, M, state))

for M, N, state in Query:
    Inv = list(zip(*state))
    Inv.sort(reverse=True, key=lambda x:max(x))
    Maxind = [-1]*N
    for i, inv in enumerate(Inv):
        m = max(inv)
        for j in range(M):
            if inv[j] == m:
                Maxind[i] = j
                break
    ans = 0
    for Ps in permutations(range(1,M), min(M, N)-1):
        Max = list(Inv[0])
        for i,p in enumerate(Ps):
            for j in range(M):
                Max[j] = max(Max[j], Inv[i+1][(Maxind[i]+j+p)%M])
        ans = max(ans, sum(Max))
    print(ans)