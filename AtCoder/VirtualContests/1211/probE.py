import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

dp = [0]*(2*10**5)
mod = 10**9+7
for a in A:
    L = 2**(a.bit_length())
    B = [0]*L
    for l in range(L):
        B[l] = dp[l^a]
    for l in range(L):
        dp[l] = (dp[l] + B[l]) % mod
    dp[a] += 1
if K == 0: dp[K] += 1
print(dp[K]%mod)