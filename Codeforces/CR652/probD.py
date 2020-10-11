import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]


mod = 10**9+7
MAX = 2*10**6+1
#MAX = 100
dp = [[0, 0] for _ in range(MAX)]


for i in range(3, MAX):
    if i % 3 == 0:
        dp[i][0] = (dp[i-1][0] + 2 * dp[i-2][1]) % mod
    elif i%3 == 1:
        dp[i][0] = (dp[i-1][1] + 2 * dp[i-2][0]) % mod
    else:
        dp[i][0] = (dp[i-1][1] + 2 * dp[i-2][1] ) % mod
    dp[i][1] = (dp[i-1][0] + 2 * dp[i-2][0] + 1) % mod

for n in Query:
    if n%3 != 2:
        ans = dp[n][1]*4 % mod
    else:
        ans = dp[n][0]*4 % mod
    print(ans)