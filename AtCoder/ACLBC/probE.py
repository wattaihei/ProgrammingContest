mod = 998244353

# 足す時はi番目に足し、返すのは累積和
class sumBIT():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for _ in range(self.N+1)]
    
    def __str__(self):
        ret = []
        for i in range(1, self.N+1):
            ret.append(self.__getitem__(i))
        return "[" + ", ".join([str(a) for a in ret]) + "]"

    def __getitem__(self, i):
        s = 0
        while i > 0:
            s = (s + self.bit[i]) % mod
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.N:
            self.bit[i] = (self.bit[i] + x) % mod
            i += i & -i

import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
LRD = [list(map(int, input().split())) for _ in range(Q)]

S = [[0]*(N+1) for _ in range(10)]
for n in range(1, 10):
    for i in range(N):
        S[n][i+1] = (S[n][i]*10 + n) % mod

bit = sumBIT(N+1)
num = 1
for i in range(1, N+1):
    bit.add(i, num)
    num = (num * 10) % mod

for l, r, d in LRD:
    l, r = N+1-r, N+1-l
    