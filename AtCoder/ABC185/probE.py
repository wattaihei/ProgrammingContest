
def main():
    import sys
    input = sys.stdin.buffer.readline

    INF = 10**18

    N, M = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))

    dp = [[INF]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = i+1
    for j in range(M):
        dp[0][j+1] = j+1

    for i, a in enumerate(A):
        for j, b in enumerate(B):
            dp[i+1][j+1] = min(dp[i+1][j+1],min(dp[i][j+1]+1, dp[i+1][j]+1))
            if a==b:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
            else:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+1)

    # L2 = max(N, M)

    print(dp[N][M])

if __name__ == "__main__":
    main()