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
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.N:
            self.bit[i] += x
            i += i & -i

import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
Q = int(input())
Query = [list(map(str, input().split())) for _ in range(Q)]

Alp = [chr(i) for i in range(97, 97+26)]
BITs = {}
for i, a in enumerate(Alp):
    bit = sumBIT(N+3)
    BITs[a] = bit

for i, s in enumerate(S):
    BITs[s].add(i+2, 1)

for WWW, x, y in Query:
    if WWW == "1":
        i = int(x)
        for alp in Alp:
            if BITs[alp][i+1] - BITs[alp][i] > 0:
                BITs[alp].add(i+1, -1)
                break
        BITs[y].add(i+1, 1)
    else:
        l = int(x)
        r = int(y)
        ans = 0
        for alp in Alp:
            if BITs[alp][r+1] - BITs[alp][l] > 0:
                ans += 1
        print(ans)