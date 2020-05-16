N, K = map(int, input().split())
A = list(map(int, input().split()))

L = 50*50
dp = [[0 for _ in range(L+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    a = A[i]
    for j in reversed(range(N)):
        for l in range(L+1):
            if l < a: continue
            dp[j+1][l] += dp[j][l-a]

ans = 0
for j in range(N):
    ans += dp[j+1][(j+1)*K]
print(ans)