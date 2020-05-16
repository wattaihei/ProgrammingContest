import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, K, A))

for N, K, A in Query:
    ans = 0
    for i, a in enumerate(A):
        cost = i*a
        if cost <= K:
            ans += a
            K -= cost
        else:
            ans += K//i
            break
    print(ans)