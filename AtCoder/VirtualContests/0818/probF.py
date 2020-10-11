import sys
input = sys.stdin.readline
import math
import copy
N, K = map(int, input().split())

mod = 10**9+7

if N == 1:
    ans = 1
else:
    Keys = set()
    for n in range(1, int(math.sqrt(N))+2):
        Keys.add(n)
        Keys.add(N//n)

    L = sorted(list(Keys))
    Counts = {1: 1}
    for i in range(len(L)-1):
        Counts[L[i+1]] = L[i+1]-L[i]

    dp = copy.copy(Counts)
    for _ in range(K-1):
        sdp = {}
        c = 0
        for l in L:
            c = (c + dp[l]) % mod
            sdp[l] = c

        for l in L:
            r = N//l
            dp[l] = sdp[r] * Counts[l] % mod

    ans = 0
    for v in dp.values():
        ans = (ans + v) % mod
print(ans)