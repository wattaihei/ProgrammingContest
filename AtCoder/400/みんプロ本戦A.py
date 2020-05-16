S = input()
T = 'yahoo'
L = len(S)

dp = [[0 for _ in range(6)] for _ in range(L+1)]

for i in range(L+1):
    dp[i][0] = i
for i in range(6):
    dp[0][i] = i

for i in range(1, L+1):
    for j in range(1, 6):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min([dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1])
        
ans = L
for i in range(6):
    ans = min(ans, dp[L][i])
print(ans)