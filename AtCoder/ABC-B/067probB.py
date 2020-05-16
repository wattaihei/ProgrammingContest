N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0
for k in range(K):
    ans += A[k]
print(ans)