import sys
input = sys.stdin.readline

def main():
    N, M, R = map(int, input().split())
    Rs = list(map(int, input().split()))

    INF = 100000*200*200
    dp = [[INF for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        dp[a-1][b-1] = c
        dp[b-1][a-1] = c

    for i in range(N):
        for j in range(N):
            for k in range(N):
                dp[j][k] = min(dp[j][k], dp[j][i]+dp[i][k])


    def ind(i, R, rem, l, ans):
        if i == R:
            ans.append(l)
            return ans
        for r in rem:
            nl = l[:]
            nl.append(r)
            nr = rem[:]
            nr.remove(r)
            ans = ind(i+1, R, nr, nl, ans)
        return ans

    inds = ind(0, R, [i for i in range(R)], [], [])

    for k, ind in enumerate(inds):
        D = 0
        for j in range(R-1):
            D += dp[Rs[ind[j]]-1][Rs[ind[j+1]]-1]
        if k == 0:
            ans = D
        ans = min(ans, D)
    print(ans)

if __name__ == "__main__":
    main()