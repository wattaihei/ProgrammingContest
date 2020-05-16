import sys
input = sys.stdin.readline

mod = 10**9+7

Q = int(input())
Query = []
for _ in range(Q):
    X = int(input())
    S = input().rstrip()
    Query.append((X, S))

for X, S in Query:
    L = len(S)
    for l in range(X):
        repeat = int(S[l])-1
        if repeat == 0:
            continue
        k = L-l-1
        if k < 0: k += mod
        if len(S) < X:
            E = S[l+1:]
        for _ in range(repeat):
            if len(S) < X:
                S += E
            L = (L + k) % mod
    print(L)