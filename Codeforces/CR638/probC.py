import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    S = list(input().rstrip())
    Query.append((N, K, S))

for N, K, S in Query:
    S.sort()
    ind = 0
    if S[0] != S[K-1]:
        print(S[K-1])
    else:
        ans = S[K-1]
        if K == N:
            print(ans)
        elif S[K] == S[N-1]:
            ans += S[K]*((N-K+K-1)//K)
            print(ans)
        else:
            ans += "".join(S[K:])
            print(ans)