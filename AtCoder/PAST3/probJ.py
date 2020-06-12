import sys
input = sys.stdin.readline
from bisect import bisect_right
INF = 10**15

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [INF]*N
for a in A:
    ind = bisect_right(dp, -a)
    if ind == N:
        print(-1)
    else:
        print(ind+1)
        dp[ind] = -a
