N = input()
L = len(N)

dp = [[[0, 0] for _ in range(L+1)] for _ in range(L+1)]
dp[0][0][0] = 1

for l in range(L):
    a = int(N[l])
    for isless in [0, 1]:
        for k in range(L):
            for num in range(10):
                if num < a:
                    if num == 1:
                        dp[l+1][k+1][1] += dp[l][k][isless]
                    else:
                        dp[l+1][k][1] += dp[l][k][isless] 
                elif num == a or isless:
                    if num == 1:
                        dp[l+1][k+1][isless] += dp[l][k][isless]
                    else:
                        dp[l+1][k][isless] += dp[l][k][isless]
#print(dp)
ans = 0
for k in range(L+1):
    ans += k*(dp[L][k][1] + dp[L][k][0])
print(ans)