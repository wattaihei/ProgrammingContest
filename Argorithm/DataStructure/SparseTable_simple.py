# 構築O(NlogN)、クエリO(1)のRMQ
# 変更はできない
# インデックスなし
class SparseTable():
    def __init__(self, N, A):
        self.N = N
        self.logN = N.bit_length()
        self.A = A
        self.table = [[0]*(self.N-(1<<k)+1) for k in range(self.logN+1)]
        self.table[0] = A
        for k in range(self.logN):
            for i in range(self.N-(1<<(k+1))+1):
                a1 = self.table[k][i]
                a2 = self.table[k][i+(1<<k)]
                if a1 <= a2:
                    self.table[k+1][i] = a1
                else:
                    self.table[k+1][i] = a2
    
    # [l, r)のminの(val, key)
    def query_min(self, l, r):
        k = (r-l).bit_length()-1
        a1 = self.table[k][l]
        a2 = self.table[k][r-(1<<k)]
        if a1 < a2:
            return a1
        return a2
    
"""
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

SP = SparseTable(N, A)

for l, r in Query:
    v = SP.query_min(l, r+1)
    print(v)
"""