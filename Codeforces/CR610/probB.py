import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, P, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, P, K, A))

for N, P, K, A in Query:
    A.sort()
    DP = [0]*N
    ans = 0
    for i, a in enumerate(A):
        if i == 0:
            DP[i] = a
        elif i < K-1:
            DP[i] = DP[i-1] + a
        else:
            DP[i] = DP[i-K] + a
        if DP[i] <= P:
            ans = i+1
    print(ans)
    