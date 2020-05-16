import sys
input = sys.stdin.readline

mod = 10**9+7

N, K = map(int, input().split())

A = [0]
for i in range(1, N+1):
    A.append((A[-1]+i)%mod)

ans = 0
for k in range(K, N+2):
    if k == N+1:
        ans = (ans + 1)%mod
    else:
        ans = (ans + (A[-1]-A[-k-1]) - A[k-1] + 1) % mod
print(ans)