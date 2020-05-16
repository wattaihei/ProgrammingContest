N = int(input())
mod = int(1E9+7)

dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            dp[2][i][j][k] = 1
dp[2][2][1][0] = 0
dp[2][1][2][0] = 0
dp[2][2][0][1] = 0

for i in range(3, N):
    for x in range(4):
        for y in range(4):
            dp[i][0][x][y] = dp[i-1][x][y][0] + dp[i-1][x][y][1] + dp[i-1][x][y][2] + dp[i-1][x][y][3]
            dp[i][1][x][y] = dp[i-1][x][y][0] + dp[i-1][x][y][1] + dp[i-1][x][y][2] + dp[i-1][x][y][3]
            dp[i][2][x][y] = dp[i-1][x][y][0] + dp[i-1][x][y][1] + dp[i-1][x][y][2] + dp[i-1][x][y][3]
            dp[i][3][x][y] = dp[i-1][x][y][0] + dp[i-1][x][y][1] + dp[i-1][x][y][2] + dp[i-1][x][y][3]
    
    dp[i][2][3][1] -= dp[i-1][3][1][0]
    dp[i][2][1][3] -= dp[i-1][1][3][0]
    dp[i][2][0][1] -= dp[i-1][0][1][0]
    dp[i][2][1][0] -= dp[i-1][1][0][0]
    dp[i][2][1][1] -= dp[i-1][1][1][0]
    
    dp[i][1][2][0] = 0
    dp[i][2][0][1] = 0
    dp[i][2][1][0] = 0
    
    


ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans = (ans + dp[N-1][i][j][k]) % mod
print(ans)