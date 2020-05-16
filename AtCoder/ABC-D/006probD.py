import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]
INF = 10**13

l = 0
dp = [INF]*(N+1)
for a in A:
    i = bisect_left(dp, a)
    if i+1 > l:
        l = i+1
    dp[i] = a

print(N-l)