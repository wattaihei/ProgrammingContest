N = int(input())
H1 = list(map(int, input().split()))
H2 = list(map(int, input().split()))

dp = [0 for _ in range(N)]

pre = 0
for n in range(N):
    print(pre)
    print(dp)
    h1, h2 = H1[n], H2[n]
    if h1 > h2:
        ppre = 1
    elif h1 < h2:
        ppre = 2
    else:
        ppre = 3
    if n == 0:
        dp[n] = max(h1, h2)
        pre = ppre
        continue
    if n > 1:
        dp[n] = dp[n-2]+max(h1, h2)
    if pre == 1 and dp[n-1]+h2 > dp[n]:
        dp[n] = dp[n-1] + h2
        if ppre != 3:
            ppre = 2
    if pre == 2 and dp[n-1]+h1 > dp[n]:
        dp[n] = dp[n-1] + h1
        if ppre != 3:
            ppre = 1
    if pre == 3:
        dp[n] = dp[n-1]+max(h1, h2)
    pre = ppre
print(dp[-1])