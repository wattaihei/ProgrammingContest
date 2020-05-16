import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    a = max(A)
    b = min(A)
    if K in set(A):
        ans = 1
    elif a < K:
        ans = (K+a-1)//a
    else:
        ans = 2
    print(ans)