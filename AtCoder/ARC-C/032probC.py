import sys
input = sys.stdin.readline
from operator import itemgetter

M = 10**6+1

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

sAB = sorted([(i, a, b) for i, (a, b) in enumerate(AB)], key=itemgetter(2))
AB.sort(key=itemgetter(0))

dp = [0]*(M+1)
ind = N-1
for m in reversed(range(M)):
    dp[m] = dp[m+1]
    while ind >= 0:
        a, b = AB[ind]
        if a == m:
            if dp[m] < dp[b] + 1:
                dp[m] = dp[b]+1
            ind -= 1
        else:
            break

L = dp[0]
dp2 = [0]*(L+1) # 残りiこ
ans = [N+1]*L
for i, a, b in sAB:
    if dp[a] == dp[b]+1 and dp2[dp[a]] <= a and ans[L-1-dp[b]] > i:
        ans[L-1-dp[b]] = i
        dp2[dp[b]] = b
print(L)
print(" ".join([str(i+1) for i in ans]))