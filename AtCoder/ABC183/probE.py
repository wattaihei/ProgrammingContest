import sys
input = sys.stdin.readline


def main():
    mod = 10**9+7

    H, W = map(int, input().rstrip().split())
    Ss = [list(input().rstrip()) + ["#"] for _ in range(H)]
    Ss.append(list("#"*(W+1)))

    dp = [[[0]*(W+1) for _ in range(H+1)] for _ in range(4)]

    dp[0][0][0] = 1
    dp[1][0][0] = 1
    dp[2][0][0] = 1
    dp[3][0][0] = 1

    for h in range(H):
        for w in range(W):
            if Ss[h][w] == ".":
                dp[1][h][w] = (dp[1][h-1][w] + dp[0][h][w]) % mod
                dp[2][h][w] = (dp[2][h][w-1] + dp[0][h][w]) % mod
                dp[3][h][w] = (dp[3][h-1][w-1] + dp[0][h][w]) % mod
                if Ss[h+1][w] == ".":
                    dp[0][h+1][w] = (dp[0][h+1][w] + dp[1][h][w]) % mod
                if Ss[h][w+1] == ".":
                    dp[0][h][w+1] = (dp[0][h][w+1] + dp[2][h][w]) % mod
                if Ss[h+1][w+1] == ".":
                    dp[0][h+1][w+1] = (dp[0][h+1][w+1] + dp[3][h][w]) % mod                 

    print(dp[0][H-1][W-1])

if __name__ == "__main__":
    main()