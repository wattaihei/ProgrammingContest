class BIT():
    def __init__(self, max):
        self.max = max
        self.data = [0]*(self.max+1)
    
    # 0からiまでの区間和
    # 立っているビットを下から処理
    def query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    # i番目の要素にxを足す
    # 覆ってる区間すべてに足す
    def add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = [None]*(N+1)
for i, a in enumerate(A):
    B[a] = i+1

bit = BIT(N)
for n in range(1, N+1):
    bit.add(n, 1)

ans = 0
for n in range(1, N+1):
    a = B[n]
    bit.add(a, -1)
    b = bit.query_sum(a)
    ans += min(b, N-n-b)
print(ans)