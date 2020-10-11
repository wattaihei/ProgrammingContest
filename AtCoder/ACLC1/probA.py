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
input = sys.stdin.buffer.readline

N = int(input())
XY = []
XtoI = [-1]*(N+1)
for i in range(N):
    x, y = map(int, input().split())
    XtoI[x] = i
    XY.append((x, y))

scoreX = [1]*(N+1)

XY.sort()

bit1 = sumBIT(N)
Maxy1 = [0]*(N+2)
for x, y in reversed(XY):
    Maxy1[x] = max(Maxy1[x+1], y)
for x, y in XY:
    scoreX[x] += bit1[Maxy1[x]]
    bit1.add(y, 1)

bit2 = sumBIT(N)
Miny2 = [N+1]*(N+2)
for x, y in XY:
    Miny2[x] = min(Miny2[x-1], y)
for x, y in reversed(XY):
    scoreX[x] += (N-x) - bit2[Miny2[x]]
    bit2.add(y, 1)

ans = [-1]*N
for x in range(1, N+1):
    ans[XtoI[x]] = str(scoreX[x])

print("\n".join(ans))