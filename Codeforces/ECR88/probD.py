import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

INF = 10**12

ans = -INF
dp = [-INF]*(62)
for i, a in enumerate(A):
    ndp = [-INF]*62
    ndp[a] = max(0, dp[a]+a)
    for k in range(-30, a):
        ndp[a] = max(ndp[a], dp[k]+k)
    for k in range(a+1, 31):
        ndp[a] = max(ndp[a], dp[k]+a)
    ans = max(ans, ndp[a])

    for k in range(a+1, 31):
        ndp[k] = dp[k]+a
        ans = max(ans, ndp[k])
    dp = ndp

print(ans)