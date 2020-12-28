import sys
input = sys.stdin.buffer.readline

mod = 998244353

def main():
    N, K = map(int, input().rstrip().split())

    dp = [0]*(N+1)
    dp[0] = 1
    for n in range(N):
        ndp = [0]*(N+1)
        for k in reversed(range(N+1)):
            if 2*k <= N:
                ndp[k] = (ndp[k] + ndp[2*k]) % mod
            if k > 0:
                ndp[k] = (ndp[k] + dp[k-1]) % mod
        dp = ndp[:]

    print(dp[K])


if __name__ == "__main__":
    main()