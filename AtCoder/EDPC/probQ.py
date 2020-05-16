# SegmantTreeの実装
import sys
input = sys.stdin.readline

# 初期化最大値
INF = (1 << 31) - 1

class SegmentTree:
    def __init__(self, N):
        self.N = 2**(N-1).bit_length()
        self.data = [[0, -1] for _ in range(2*self.N-1)]

    # k番目の値をget
    def get(self, k):
        k += self.N - 1
        s = self.data[k][0]
        while k > 0:
            k = (k-1)//2
            s = max(s, self.data[k][0])
        return s

    def update(self, l, x):
        L = l + self.N
        R = 2*self.N
        while L < R:
            if R & 1:
                R -= 1
                if x > self.data[R-1][0]:
                    self.data[R-1][0] = x
            if L & 1:
                if x > self.data[L-1][0]:
                    self.data[L-1][0] = x
                L += 1
            L >>= 1; R >>= 1

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

ST = SegmentTree(N+1)

ans = 0
for h, a in zip(H, A):
    m = ST.get(h)
    ans = max(ans, m+a)
    ST.update(h, m+a)

print(ans)