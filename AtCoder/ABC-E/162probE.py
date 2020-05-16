import sys
input = sys.stdin.readline

mod = 10**9+7

N, K = map(int, input().split())

ans = 0
dp = [None]*(K+1)
for n in reversed(range(1, K+1)):
    L = K//n
    p = pow(L, N, mod)
    for i in range(2, L+1):
        p = (p - dp[n*i]) % mod
    
    dp[n] = p
    ans = (ans + p*n) % mod

print(ans)