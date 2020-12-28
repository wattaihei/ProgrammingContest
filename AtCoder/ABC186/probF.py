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

MAX = 2*10**5

H ,W, M = map(int, input().rstrip().split())
Xs = [[] for _ in range(MAX+1)]
Ys = [[] for _ in range(MAX+1)]
for _ in range(M):
    x, y = map(int, input().rstrip().split())
    Xs[x].append(y)
    Ys[y].append(x)

ans = 0

s = set()
m = min(Xs[1])-1 if Xs[1] else W
for x in range(1, H+1):
    for y in Xs[x]:
        if y <= m:
            s.add(y)
    ans += m - len(s)

s = set()
m = min(Ys[1])-1 if Ys[1] else H
for y in range(1, W+1):
    for x in Ys[y]:
        if x <= m:
            s.add(x)
    ans += m - len(s)

ymax = min(Xs[1])-1 if Xs[1] else W
xmax = min(Ys[1])-1 if Ys[1] else H

bit = sumBIT(ymax+1)

for x in range(1, xmax+1):
    left = ymax+1
    a = 0
    for y in Xs[x]:
        if y <= ymax:
            if bit[y] - bit[y-1] == 0:
                bit.add(y, 1)
            a += 1
        left = min(left, y)
    c = bit[left-1]
    ans -= (left-1) - c



print(ans)