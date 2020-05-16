N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

A0 = A[:K]
A1 = A[N-K:]

ans = K
for i in range(K):
    ans += A0[i]/A1[i]

print(ans)