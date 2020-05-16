import math
N, M = map(int, input().split())
mod = int(1E9+7)

def prime(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor

dp = [[1 for _ in range(30)] for _ in range(N)]

for j in range(1, 30):
    for i in range(1, N):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod

A = prime(M)

ans = 1
for x in A.values():
    ans *= dp[N-1][x]
    ans = ans % mod
print(ans)