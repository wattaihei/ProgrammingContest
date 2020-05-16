INF = 10**14

class BIT():
    def __init__(self, max):
        self.max = max
        self.data = [INF]*(self.max+1)
    
    def query_min(self, i):
        s = INF
        while i <= self.max:
            if s > self.data[i]:
                s = self.data[i]
            i += i & -i
        return s

    def update(self, i, x):
        while i > 0:
            if x < self.data[i]:
                self.data[i] = x
            i -= i & -i

import sys
input = sys.stdin.readline
from operator import itemgetter

N, L = map(int, input().split())
LRC = [list(map(int, input().split())) for _ in range(N)]

LRC.sort(key=itemgetter(0))

bit = BIT(L)
for l, r, c in LRC:
    if l == 0:
        bit.update(r, c)
    else:
        lowest = bit.query_min(l)
        bit.update(r, lowest+c)

print(bit.query_min(L))