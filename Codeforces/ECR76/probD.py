import sys
input = sys.stdin.readline
from bisect import bisect_left

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    state = [list(map(int, input().split())) for _ in range(M)]
    Query.append((N, A, M, state))

for N, A, M, state in Query:
    state.sort()
    P = []
    S = []
    for p, s in state:
        P.append(p)
        S.append(s)
    
    for i in reversed(range(M-1)):
        S[i] = max(S[i], S[i+1])
    
    ans = 0
    now = 10**12
    tm_max = 0
    for a in reversed(A):
        i = bisect_left(P, max(a, tm_max))
        if i == M:
            ans = -1
            break
        if now + 1 > S[i]:
            tm_max = a
            now = 1
            ans += 1
        else:
            tm_max = max(tm_max, a)
            now += 1
    print(ans)