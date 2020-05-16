import sys
input = sys.stdin.readline
import numpy as np

mod = 998244353
N = int(input())
A = [int(input()) for _ in range(N)]

L = sum(A)//2
dp1 = np.zeros((L+1,), dtype=int)
dp2 = np.zeros((L+1,), dtype=int)
dp1[0] = 1
dp2[0] = 1
for a in A:
    if a >= L+1: continue
    dp1 = (dp1 + np.concatenate((np.zeros((a,), dtype=int), dp1[:L+1-a]))) % mod
    dp2 = (dp2 + np.concatenate((np.zeros((a,), dtype=int), 2*dp2[:L+1-a]))) % mod

p1 = 0
p2 = 0
for s in range(1,L+1):
    p1 = (p1 + dp1[s]*6)%mod
    p2 = (p2 + dp2[s]*3)%mod
ans = (pow(3, N, mod) + 3 - 3*pow(2, N, mod) - p2 + p1) % mod
print(ans)