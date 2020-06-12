import sys
input = sys.stdin.readline
mod = 10**9+7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    L = max(A[-1], X)

    dp = [[0]*N for _ in range(L+1)]
    a = A[0]
    for x in range(L+1):
        dp[x][0] = x%a

    dp1 = [0 for _ in range(L+1)] #累積和見たいな
    for n in range(1, N):
        a = A[n]
        for x in range(L+1):
            dp1[x] = ((n-1) * dp1[x] + dp[x][n-1]) % mod
            dp[x][n] = dp1[x%a]

    ans = 0
    t = 1
    for n in reversed(range(N)):
        ans = (ans + dp[X][n]*t) % mod
        t = t * n % mod

    print(ans)


if __name__ == "__main__":
    main()