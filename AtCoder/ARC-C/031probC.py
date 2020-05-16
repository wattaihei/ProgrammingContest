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

bit1 = BIT(N)
B1 = [0]
for i, a in enumerate(A):
    b = bit1.query_sum(a)
    B1.append(B1[-1]+(i-b))
    bit1.add(a, 1)

bit2 = BIT(N)
B2 = [0]
for i, a in enumerate(reversed(A)):
    b = bit2.query_sum(a)
    B2.append(B2[-1]+(i-b))
    bit2.add(a, 1)

ans = 10**14
for n in range(N+1):
    c = B1[n] + B2[N-n]
    if c < ans:
        ans = c

print(ans)