import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    A.sort()
    ans = 10**18
    for i in range(N-1):
        ans = min(ans, A[i+1]-A[i])
    print(ans)