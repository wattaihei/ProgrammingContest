import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, M, K, A))

INF = 10**14

for N, M, K, A in Query:
    ans = 0
    M -= 1
    if K <= M:
        remain = M - K
        for left in range(K+1):
            length = N - left - (K-left) - remain
            score = INF
            for r in range(remain+1):
                score = min(max(A[left+r], A[left+r+length-1]), score)
            ans = max(ans, score)
    else:
        ans = max(A[:M+1] + A[N-M-1:])
    print(ans)