import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    ans = 0
    for a in A:
        if a == 0:
            ans += 1
    if sum(A) + ans == 0:
        ans += 1
    print(ans)