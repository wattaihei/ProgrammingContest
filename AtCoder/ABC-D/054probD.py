
def main():
    N, Ma, Mb = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]

    INF = 10000000

    dp = [[[INF for _ in range(10*N)] for _ in range(10*N)] for _ in range(N)]

    for i, (a, b, c) in enumerate(ABC):
        a -= 1
        b -= 1
        if i == 0:
            dp[0][a][b] = c
            continue
        for ai in range(10*N):
            for bi in range(10*N):
                if a > ai or b > bi:
                    dp[i][ai][bi] = dp[i-1][ai][bi]
                elif ai == a and bi == b:
                    dp[i][ai][bi] = min(dp[i-1][ai][bi], c)
                else:
                    dp[i][ai][bi] = min(dp[i-1][ai-a-1][bi-b-1]+c, dp[i-1][ai][bi])

    ans = INF
    for i in range(10*N):
        for j in range(10*N):
            if (i+1)*Mb == (j+1)*Ma:
                #print(i, j, dp[N-1][i][j])
                ans = min(dp[N-1][i][j], ans)
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()