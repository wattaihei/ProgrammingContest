import sys
input = sys.stdin.buffer.readline

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

N, Q = map(int, input().split())
C = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

Toask = [[] for _ in range(N+1)]
for i, (l, r) in enumerate(LR):
    Toask[l].append((r, i))

bit = sumBIT(N+3)
ans = [-1]*Q

Color = [-1]*(N+1)
for l in reversed(range(1, N+1)):
    c = C[l-1]
    if Color[c] != -1:
        last = Color[c]
        bit.add(last, -1)
    bit.add(l, 1)
    for r, ind in Toask[l]:
        ans[ind] = str(bit[r])
    Color[c] = l

print("\n".join(ans))