import sys
input = sys.stdin.readline
import math

mod = 10**9+7
N, K = map(int, input().split())
K -= 1

P = set()
inv = {}
for i in range(1, int(math.sqrt(N)+2)):
    if i**2 > N: break
    P.add(i)
    P.add(N//i)
    if i not in inv:
        inv[i] = N//i
    if N//i not in inv:
        inv[N//i] = i

P1 = sorted(list(P))

T = len(P1)

M = [1]
for i in range(T-1):
    M.append(P1[i+1]-P1[i])


co_to_ind = {}
for i, p in enumerate(P1):
    co_to_ind[p] = i

Inv = []
for p in P1:
    Inv.append(co_to_ind[inv[p]])

dp = [[0]*T for _ in range(K+1)]

dp[0] = M

for i in range(K):
    tosum = [0]*T
    for ik in range(T):
        j = Inv[ik]
        tosum[j] = (tosum[j] + dp[i][ik]) % mod

    sumup = 0
    for ik in reversed(range(T)):
        sumup = (sumup + tosum[ik]) % mod
        dp[i+1][ik] = sumup * M[ik] % mod

ans = 0
for t in range(T):
    ans = (ans + dp[K][t]) % mod

print(ans)