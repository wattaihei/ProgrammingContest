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

import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = sorted(list(Counter(A).values()), reverse=True)
L = len(C)
B = BITbisect(list(range(L+1)))

num = C[0]
for i, c in enumerate(C):
    for _ in range(num-c):
        B.push(i+1)
    num = c
for _ in range(num):
    B.push(L)

ans = [N]
for n in range(2, N+1):
    if n > L:
        ans.append(0)
        continue
    # ans求める
    used = []
    for _ in range(N):
        ind = B.bisect_right(n)
        if ind == len(B):
            if B[ind-1] == n:
                B.delete(n)
                used.append(n)
            else:
                break
        elif ind == 0:
            num_r = B[0]
            B.delete(num_r)
            B.push(num_r-n)
            used.append(0)
        else:
            num_l = B[ind-1]
            num_r = B[ind]
            B.delete(num_l)
            used.append(num_l)
            delta = n-num_l
            if delta > 0:
                B.delete(num_r)
                B.push(num_r-delta)
    ans.append(len(used))
    # 復元
    for num in reversed(used):
        if num == 0:
            b = B[0]
            B.delete(b)
            B.push(b+n)
        elif num == n:
            B.push(n)
        else:
            ib = B.
