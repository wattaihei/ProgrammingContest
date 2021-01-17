mod = 10**9+7

import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

X = 0
for a in A:
    X ^= a

if X == 0:
    pass
else:
    x = 0
    dp = [1, 0]
    for a in A:
        x ^= a
        if x == X:
            dp[1] = (dp[1] + dp[0]) % mod
        elif x == 0:
            dp[0] = (dp[1] + dp[0]) % mod
    ans = dp[1]

print(ans)