Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    A.sort(reverse=True)
    ans = 1
    for n in range(N):
        if n+1 > A[n]:
            break
        ans = n+1
    print(ans)