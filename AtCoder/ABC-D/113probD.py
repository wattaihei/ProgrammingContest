H, W, K = map(int, input().split())
mod = int(1E9+7)

if W == 1:
    print(1)
else:
    dp = [[0 for _ in range(W)] for _ in range(H+1)]

    P = [1, 1, 2, 3, 5, 8, 13, 21]
    dp[0][0] = 1

    for h in range(1, H+1):
        for k in range(W):
            if k == 0:
                dp[h][k] = (P[k]*P[W-k-1]*dp[h-1][k] + P[k]*P[W-k-2]*dp[h-1][k+1]) % mod
            elif k == W-1:
                dp[h][k] = (P[k-1]*P[W-k-1]*dp[h-1][k-1] + P[k]*P[W-k-1]*dp[h-1][k]) % mod
            else:
                dp[h][k] = (P[k-1]*P[W-k-1]*dp[h-1][k-1] + P[k]*P[W-k-1]*dp[h-1][k] + P[k]*P[W-k-2]*dp[h-1][k+1]) % mod
    print(dp[H][K-1])
