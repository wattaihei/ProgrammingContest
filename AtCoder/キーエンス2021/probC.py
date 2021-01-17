

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    r = "R"
    d = "D"
    x = "X"

    mod = 998244353

    H, W, K = map(int, input().rstrip().split())
    state = [[0]*W for _ in range(H)]
    for _ in range(K):
        str_h, str_w, c = input().rstrip().split()
        h = int(str_h)-1; w = int(str_w)-1
        state[h][w] = c
    
    weight = pow(3, H*W-K, mod)

    two = pow(3, mod-2, mod) * 2 % mod
    
    dp = [[0]*(W+1) for _ in range(H+1)]
    dp[0][0] = weight
    for h in range(H):
        for w in range(W):
            c = state[h][w]
            if c == r:
                dp[h][w+1] = (dp[h][w+1] + dp[h][w]) % mod
            elif c == d:
                dp[h+1][w] = (dp[h+1][w] + dp[h][w]) % mod
            elif c == x:
                dp[h][w+1] = (dp[h][w+1] + dp[h][w]) % mod 
                dp[h+1][w] = (dp[h+1][w] + dp[h][w]) % mod
            else:
                dp[h][w+1] = (dp[h][w+1] + two*dp[h][w]) % mod 
                dp[h+1][w] = (dp[h+1][w] + two*dp[h][w]) % mod
    
    print(dp[H-1][W-1])