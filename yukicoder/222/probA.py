import sys
input = sys.stdin.readline

# 初期化最大値
INF = 10**9

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

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]

ST = SegmentTree(N)

for i, a in enumerate(A):
    ST.update(i, a)

for com, l, r in Query:
    l -= 1
    r -= 1
    if com == 1:
        al = ST.query_min(l, l+1)[0]
        ar = ST.query_min(r, r+1)[0]
        ST.update(l, ar)
        ST.update(r, al)
    else:
        print(ST.query_min(l, r+1)[1]+1)