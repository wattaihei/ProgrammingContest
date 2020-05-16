import sys
input = sys.stdin.readline

def main():
    N = int(input())
    graph = [[int(a) for a in list(input().rstrip())] for _ in range(N)]
    M = int(input())
    P = list(map(int, input().split()))

    INF = 10**16
    dp = [[None]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                dp[i][j] = 0
            elif graph[i][j] == 0:
                dp[i][j] = INF
            else:
                dp[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

    ans = [P[0]]
    last = 0
    for i in range(1, M):
        p0, p1 = P[i-1], P[i]
        if dp[ans[-1]-1][p1-1]< i + 1 - last:
            ans.append(p0)
            last = i
    ans.append(P[M-1])
    ans = ans[1:]

    print(len(ans))
    print(' '.join([str(a) for a in ans]))


if __name__ == "__main__":
    main()