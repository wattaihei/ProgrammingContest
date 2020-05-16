import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    INF = int(1E8)
    dp = [INF for _ in range(2**N)]
    A = [None for _ in range(M)]
    for j in range(M):
        a, b = map(int, input().split())
        C = list(map(int, input().split()))
        ind = 0
        for c in C:
            ind += 2**(c-1)
        A[j] = (ind, a)
        dp[ind] = min(dp[ind], a)

    Id = [i for i in range(2**N)]
    Id.sort(key=lambda x: bin(x).count('1'))

    for x in Id:
        for ind, a in A:
            dp[x|ind] = min(dp[x|ind], dp[x]+a)
    if dp[2**N-1] >= INF:
        print(-1)
    else:
        print(dp[2**N-1])

if __name__ == "__main__":
    main()