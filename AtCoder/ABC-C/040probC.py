N = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(1, N):
    if i == 1:
        dp[i] = abs(A[1]-A[0])
        continue
    dp[i] = min(dp[i-2]+abs(A[i]-A[i-2]), dp[i-1]+abs(A[i]-A[i-1]))
print(dp[-1])