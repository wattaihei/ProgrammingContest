import sys
input = sys.stdin.buffer.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    INF = 10**9+5

    if K%2 == 0:
        A1 = A[:-1]
        A2 = A[1:]
    else:
        A1 = A
        A2 = A[1:-1]

    def solve(B, border, m):
        dp = [[0, 0] for _ in range(len(B)+1)]
        for i, a in enumerate(B):
            if a > m:
                dp[i+1][0] = max(dp[i])
            else:
                dp[i+1][0] = max(dp[i])
                dp[i+1][1] = dp[i][0] + 1
        return max(dp[-1]) >= border

    l = 0
    r = INF
    while r-l > 1:
        m = (r+l)//2
        if K%2 == 0:
            ok = solve(A1, K//2, m) or solve(A2, K//2, m)
        else:
            ok = solve(A1, (K+1)//2, m) or solve(A2, K//2, m)
        if ok:
            r = m
        else:
            l = m

    print(r)


if __name__ == "__main__":
    main()