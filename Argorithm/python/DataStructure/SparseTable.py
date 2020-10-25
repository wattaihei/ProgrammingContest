# 構築O(NlogN)、クエリO(1)のRMQ
# 変更はできない
# インデックス付き
class SparseTable():
    def __init__(self, N, A):
        self.N = N
        self.logN = N.bit_length()
        self.A = A
        self.table = [[0]*(self.N-(1<<k)+1) for k in range(self.logN+1)]
        self.table[0] = [i for i in range(self.N)]
        for k in range(self.logN):
            for i in range(self.N-(1<<(k+1))+1):
                ind1 = self.table[k][i]
                ind2 = self.table[k][i+(1<<k)]
                if self.A[ind1] <= self.A[ind2]:
                    self.table[k+1][i] = ind1
                else:
                    self.table[k+1][i] = ind2
    
    # [l, r)のminの(val, key)
    def query_min(self, l, r):
        k = (r-l).bit_length()-1
        indl = self.table[k][l]
        indr = self.table[k][r-(1<<k)]
        if self.A[indl] <= self.A[indr]:
            return self.A[indl], indl
        return self.A[indr], indr
    