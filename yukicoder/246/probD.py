import sys
input = sys.stdin.readline
from bisect import bisect_left
mod = 10**9+7

N, M = map(int, input().split())
V = list(map(int, input().split()))
R = list(map(int, input().split()))
A, B = map(int, input().split())

Lv = sum(V)
dp1 = [0]*(Lv+1)
dp1[0] = 1
for v in V:
    for t in reversed(range(Lv+1-v)):
        dp1[t+v] = (dp1[t+v] + dp1[t]) % mod

Lr = sum(R)
dp2 = [0]*(Lr+1)
dp2[0] = 1
for r in R:
    for t in reversed(range(Lr+1-r)):
        dp2[t+r] = (dp2[t+r] + dp2[t]) % mod

dp3 = [0]*(Lv+1)
dp3[0] = dp1[0]
for n in range(Lv):
    dp3[n+1] = (dp3[n] + dp1[n+1]) % mod

ans = 0
for c in range(1, Lr+1):
    score = dp2[c] * (dp3[min(c*B, Lv)] - dp3[min(c*A-1, Lv)]) % mod
    ans = (ans + score) % mod
print(ans)