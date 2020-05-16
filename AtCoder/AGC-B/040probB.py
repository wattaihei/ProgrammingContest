import sys
input = sys.stdin.readline
from operator import itemgetter

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
LR.sort(key=itemgetter(0))

dp = [[[0, 0], [0, 0]] for _ in range(N)]

L0, R0 = LR[0]
L1, R1 = LR[1]
dp[1][0][0] = L0
dp[1][0][1] = R0
dp[1][1][0] = L1
dp[1][1][1] = R1
L, R = max(L0, L1), min(R0, R1)
for i in range(1, N-1):
    l, r = LR[i+1]
    a0 = max(min(dp[i][0][1], r) - max(dp[i][0][0], l)+1, 0) + max(dp[i][1][1] - dp[i][1][0] + 1, 0)
    a1 = max(min(dp[i][1][1], r) - max(dp[i][1][0], l)+1, 0) + max(dp[i][0][1] - dp[i][0][0] + 1, 0)
    a2 = max(R-L+1, 0) + r-l+1
    a = max(a0, a1, a2)
    if a == a2:
        dp[i+1][0][0] = l
        dp[i+1][0][1] = r
        dp[i+1][1][0] = L
        dp[i+1][1][1] = R
    elif a == a0:
        dp[i+1][0][0] = max(dp[i][0][0], l)
        dp[i+1][0][1] = min(dp[i][0][1], r)
        dp[i+1][1][0] = dp[i][1][0]
        dp[i+1][1][1] = dp[i][1][1]
    elif a == a1:
        dp[i+1][0][0] = dp[i][0][0]
        dp[i+1][0][1] = dp[i][0][1]
        dp[i+1][1][0] = max(dp[i][1][0], l)
        dp[i+1][1][1] = min(dp[i][1][1], r)
    L, R = max(L, l), min(R, r)

ans = max(dp[N-1][0][1]-dp[N-1][0][0]+1, 0) + max(dp[N-1][1][1] - dp[N-1][1][0] + 1, 0)
print(ans)