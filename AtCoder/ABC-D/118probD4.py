import sys
input = sys.stdin.readline

NUM = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
INF = 10**14

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

dp = [-INF]*(N+1)
dp[0] = 0
for i in range(N):
    for a in A:
        c = NUM[a]
        if i + c <= N:
            dp[i+c] = max(dp[i+c], dp[i]+1)

D = dp[N]
ind = N
ans = ''
for _ in range(D):
    for a in A:
        c = NUM[a]
        if ind - c < 0: continue
        if dp[ind] == dp[ind-c] + 1:
            ind -= c
            ans += str(a)
            break
print(ans)