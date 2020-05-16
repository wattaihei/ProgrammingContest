# 足す時は0~iまで一律に足し、返すのはi番目の値
class imosBIT():
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
        while i <= self.N:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, i, x):
        while i > 0:
            self.bit[i] += x
            i -= i & -i


import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = []
for _ in range(Q):
    a, b, c = map(str, input().split())
    Query.append((a=="A", int(b), int(c)))

bit = imosBIT(N)

P = []
for isA, x, y in Query:
    if isA:
        p = bit[x]
        # x番目は今pで、yをたす
        P.append((x, p, y))
    else:
        bit.add(y, 1)
        bit.add(x-1, -1)

ans = []
for i, a in enumerate(A):
    ans.append(bit[i+1]*a)

for x, p, y in P:
    ans[x-1] += y*(bit[x]-p)

print(*ans)