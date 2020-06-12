import sys
input = sys.stdin.readline

INF = 10**14

N, L = map(int, input().split())
X = set(list(map(int, input().split())))
T1, T2, T3 = map(int, input().split())

dp = [[INF, INF] for _ in range(L+6)]

dp[0][0] = 0
for x in range(L):
    if x+1 in X:
        dp[x+1][0] = min(dp[x+1][0], dp[x][0]+T1+T3)
    else:
        dp[x+1][0] = min(dp[x+1][0], dp[x][0]+T1)
    dp[x+1][1] = min(dp[x+1][1], dp[x][0]+(T1+T2)//2)
    dp[x+2][1] = min(dp[x+2][1], dp[x][0]+(T1+T2)//2+T2)
    dp[x+3][1] = min(dp[x+3][1], dp[x][0]+(T1+T2)//2+2*T2)

    if x+2 in X:
        dp[x+2][0] = min(dp[x+2][0], dp[x][0] + T1+T2+T3)
    else:
        dp[x+2][0] = min(dp[x+2][0], dp[x][0] + T1+T2)
    if x+4 in X:
        dp[x+4][0] = min(dp[x+4][0], dp[x][0] + T1+3*T2+T3)
    else:
        dp[x+4][0] = min(dp[x+4][0], dp[x][0] + T1+3*T2)

print(min(dp[L]))