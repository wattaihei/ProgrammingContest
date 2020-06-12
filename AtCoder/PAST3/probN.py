import sys
input = sys.stdin.readline

from bisect import bisect_right, bisect_left
# instead of AVLTree
class BITbisect():
    def __init__(self, InputProbNumbers):
        # 座圧
        self.ind_to_co = [-10**18]
        self.co_to_ind = {}
        for ind, num in enumerate(sorted(list(set(InputProbNumbers)))):
            self.ind_to_co.append(num)
            self.co_to_ind[num] = ind+1
        self.max = len(self.co_to_ind)
        self.data = [0]*(self.max+1)
    
    def __str__(self):
        retList = []
        for i in range(1, self.max+1):
            x = self.ind_to_co[i]
            if self.count(x):
                c = self.count(x)
                for _ in range(c):
                    retList.append(x)
        return "[" + ", ".join([str(a) for a in retList]) + "]"
    
    def __getitem__(self, key):
        key += 1
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1<<i) <= self.max:
                if s + self.data[ind+(1<<i)] < key:
                    s += self.data[ind+(1<<i)]
                    ind += (1<<i)
        if ind == self.max or key < 0:
            raise IndexError("BIT index out of range")
        return self.ind_to_co[ind+1]
    
    def __len__(self):
        return self._query_sum(self.max)
    
    def __contains__(self, num):
        if not num in self.co_to_ind:
            return False
        return self.count(num) > 0
    
    # 0からiまでの区間和
    # 左に進んでいく
    def _query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    # i番目の要素にxを足す
    # 上に登っていく
    def _add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i
    
    # 値xを挿入
    def push(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The pushing number didnt initialized")
        self._add(self.co_to_ind[x], 1)
            
    # 値xを削除
    def delete(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The deleting number didnt initialized")
        if self.count(x) <= 0:
            raise ValueError("The deleting number doesnt exist")
        self._add(self.co_to_ind[x], -1)

    # 要素xの個数
    def count(self, x):
        return self._query_sum(self.co_to_ind[x]) - self._query_sum(self.co_to_ind[x]-1)
    
    # 値xを超える最低ind
    def bisect_right(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_right(self.ind_to_co, x) - 1
        return self._query_sum(i)

    # 値xを下回る最低ind
    def bisect_left(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_left(self.ind_to_co, x)
        if i == 1:
            return 0
        return self._query_sum(i-1)


N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]


B = BITbisect(list(range(1, N+1)))
A = [i for i in range(N+1)]


for t, x, y in Query:
    if t == 1:
        if A[x] < A[x+1]:
            B.push(x)
        if x >= 2:
            if A[x-1] < A[x] and A[x-1] > A[x+1]:
                B.push(x-1)
            if A[x-1] > A[x] and A[x-1] < A[x+1]:
                B.delete(x-1)
        if x+1 < N:
            if A[x+2] > A[x+1] and A[x+2] < A[x]:
                B.push(x+1)
            if A[x+2] < A[x+1] and A[x+2] > A[x]:
                B.delete(x+1)
        A[x], A[x+1] = A[x+1], A[x]
    else:
        to_delete = []
        while len(B) > 0:
            bind = B.bisect_left(x)
            if bind == len(B): break
            b = B[bind]
            if x <= b < y:
                to_delete.append(b)
                B.delete(b)
            else:
                break
        while to_delete:
            q = []
            for w in to_delete:
                if w >= x+1:
                    if A[w-1] < A[w] and A[w-1] > A[w+1]:
                        q.append(w-1)
                if w+1 < y:
                    if A[w+2] > A[w+1] and A[w+2] < A[w]:
                        q.append(w+1)
                A[w], A[w+1] = A[w+1], A[w]
            to_delete = q

print(*A[1:])