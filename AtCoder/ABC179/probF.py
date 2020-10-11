INF = 10**18

class BITmin():
    def __init__(self, max):
        self.max = max
        self.data = [self.max-1]*(self.max+1)
    
    # 上に登ってく
    def query_min(self, i):
        s = INF
        while i <= self.max:
            if s > self.data[i]:
                s = self.data[i]
            i += i & -i
        return s

    # iまで全ての要素をxで更新
    def update(self, i, x):
        while i > 0:
            if x < self.data[i]:
                self.data[i] = x
            # i += i & -i
            i -= i & -i

import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

BitX = BITmin(N)
BitY = BITmin(N)

ans = (N-2)*(N-2)
for a, b in Query:
    b -= 1
    if a == 1:
        loc = BitX.query_min(b)
        ans -= loc-1
        BitY.update(loc, b)
    else:
        loc = BitY.query_min(b)
        ans -= loc-1
        BitX.update(loc, b)
    
print(ans)