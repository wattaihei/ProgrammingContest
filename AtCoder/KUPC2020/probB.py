import sys
input = sys.stdin.buffer.readline

mod = 10**9+7
N, K = map(int, input().split())
V = [list(map(int, input().split())) for _ in range(N)]

dp = [k for k in range(K+1)]
for i in range(1,N):
    ndp = [0]
    ind = 0
    for v in V[i]:
        while ind < K and V[i-1][ind] <= v:
            ind += 1
        ndp.append((dp[ind] + ndp[-1])%mod)
    dp = ndp

print(dp[-1])