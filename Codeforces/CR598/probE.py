# AOJ DSL_2_A "Range Minimum Query"
# SegmantTreeの実装
import sys
input = sys.stdin.readline

# 初期化最大値
INF = (1 << 31) - 1

class SegmentTree:
    def __init__(self, N):
        self.N = 2**(N-1).bit_length()
        self.data = [[INF, -1] for _ in range(2*self.N-1)]

    # k番目の値(0-indexed)をaに変更
    def update(self, k, a):
        self.data[k+self.N-1] = [a, k]
        k += self.N - 1
        while k > 0:
            k = (k-1)//2
            if self.data[2*k+1][0] < self.data[2*k+2][0]:
                self.data[k] = self.data[2*k+1][:]
            else:
                self.data[k] = self.data[2*k+2][:]

    # [l, r)の最小値取得
    # kがNodeの番号、対応する区間が[a, b)
    def query_min(self, l, r):
        L = l + self.N
        R = r + self.N
        s = [INF, -1]
        while L < R:
            if R & 1:
                R -= 1
                if s[0] > self.data[R-1][0]:
                    s = self.data[R-1]
            if L & 1:
                if s[0] > self.data[L-1][0]:
                    s = self.data[L-1]
                L += 1
            L >>= 1; R >>= 1
        return s

from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

B = []
for i, a in enumerate(A):
    B.append((i, a))
B.sort(key=itemgetter(1))

ST = SegmentTree(N)
for i in range(N):
    ST.update(i, B[i][1])

ans = [None]*N
cost = 0
if N % 3 == 0:
    for i in range(N//3):
        L = [B[3*i][1], B[3*i+1][1], B[3*i+2][1]]
        cost += max(L) - min(L)
        ans[B[3*i][0]] = i+1
        ans[B[3*i+1][0]] = i+1
        ans[B[3*i+2][0]] = i+1
elif N % 3 == 1:
    
