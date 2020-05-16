import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    A.sort(reverse=True)
    n = 0
    s = 0
    for i, a in enumerate(A):
        s += a
        if s >= (i+1)*K:
            n = i+1
    print(n)