import sys
input = sys.stdin.buffer.readline

def main():
    INF = 10**18

    N = int(input())
    XYZ = [list(map(int, input().split())) for _ in range(N)]

    Cost = [[0]*N for _ in range(N)]
    for i, (a, b, c) in enumerate(XYZ):
        for j, (p, q, r) in enumerate(XYZ):
            Cost[i][j] = abs(a-p) + abs(b-q) + max(0, r-c)

    dp = [[INF]*(1<<N) for _ in range(N)]
    dp[0][1] = 0
    for bit in range(1<<N):
        for i in range(N):
            if (1<<i)&bit:
                for j in range(N):
                    nbit = bit | (1<<j)
                    dp[j][nbit] = min(dp[j][nbit], dp[i][bit] + Cost[i][j])

    ans = INF
    for i in range(N):
        ans = min(ans, dp[i][(1<<N)-1] + Cost[i][0])
    print(ans)

if __name__ == "__main__":
    main()