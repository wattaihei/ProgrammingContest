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
A = list(map(int, input().split()))

l = 0
r = max(A) + 1
while r-l > 1:
    x = (l+r)//2
    P = [0]
    for a in A:
        p = +1 if a >= x else -1
        P.append(P[-1]+p)
    score = 0
    bit = imosBIT(2*N+5)
    for p in P:
        p += N+1
        score += bit[p]
        bit.add(p, 1)
    
    if score >= (N*(N+1)//2+1)//2:
        l = x
    else:
        r = x

print(l)