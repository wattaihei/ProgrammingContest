mod = 10**9+7

# instead of AVLTree
class BIT():
    def __init__(self, max):
        self.max = max
        self.data = [0]*(self.max+1)
    
    # 0からiまでの区間和
    # 立っているビットを下から処理
    def query_sum(self, i):
        s = 0
        while i <= self.max:
            s += self.data[i]
            s %= mod
            i += i & -i
        return s

    # i番目の要素にxを足す
    # 覆ってる区間すべてに足す
    def add(self, i, x):
        while i > 0:
            self.data[i] += x
            self.data[i] %= mod
            i -= i & -i

import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
D = [int(input()) for _ in range(N)]
D.sort()

bits = [BIT(N), BIT(N), BIT(N)]

ans = 0
for i in range(N):
    j = bisect_left(D, D[i]*2)
    count = []
    for k in range(3):
        count.append(bits[k].query_sum(i+1))
    bits[0].add(N, 1)
    bits[0].add(j, -1)
    bits[1].add(N, count[0])
    bits[1].add(j, -count[0])
    bits[2].add(N, count[1])
    bits[2].add(j, -count[1])
    ans += count[2]
    ans %= mod
print(ans)