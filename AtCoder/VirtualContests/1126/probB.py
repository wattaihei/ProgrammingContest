import sys
input = sys.stdin.buffer.readline

def main():
    N, L = map(int, input().rstrip().split())
    WV = [list(map(int, input().rstrip().split())) for _ in range(N)]

    # dp[][j][s] j個選択し、合計s
    wb = WV[0][0]
    dp = [[0]*(3*N+1) for _ in range(N+1)]
    for w, v in WV:
        dw = w - wb
        for j in reversed(range(N+1)):
            for s in reversed(range(3*N+1)):
                if j+1 <= N and s+dw <= 3*N and dp[j+1][s+dw] < dp[j][s] + v:
                    dp[j+1][s+dw] = dp[j][s] + v

    ans = 0
    for j in range(N+1):
        for s in range(3*N+1):
            if wb*j+s <= L:
                ans = max(ans, dp[j][s])

    print(ans)

if __name__ == "__main__":
    main()