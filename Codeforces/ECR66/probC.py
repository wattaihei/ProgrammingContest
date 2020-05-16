import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append([N, K, A])

INF = 10**14

for N, K, A in Query:
    A.sort()
    D = INF
    for i in range(N-K):
        if A[i+K]-A[i] < D:
            D = A[i+K]-A[i]
            ans = (A[i+K]+A[i])//2
    print(ans)