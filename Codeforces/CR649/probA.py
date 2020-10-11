import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

MAX = 10**4+3

for N, K, A in Query:
    nonzero = -1
    t = 0
    ans = 0
    for i, a in enumerate(A):
        t = (t + a) % K
        if t != 0:
            ans = max(ans, i+1)
            if nonzero == -1:
                nonzero = i
        else:
            if nonzero != -1:
                ans = max(ans, i - nonzero)
    if nonzero == -1:
        ans = -1
    print(ans)