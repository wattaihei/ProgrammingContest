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
input = sys.stdin.buffer.readline
import heapq as hp

#INF = 10**14
M = 2*10**5+3
#M = 11

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(Q)]

Grand = [[] for _ in range(M)]
Nowin = [-1]*(N+2)

In = []
for i, (a, b) in enumerate(AB):
    hp.heappush(Grand[b], (-a, i+1))
    Nowin[i+1] = b
    In.append(a)

Bit = BITbisect(In)


for i in range(M):
    if Grand[i]:
        minusrate, _ = Grand[i][0]
        Bit.push(-minusrate)

# 最新情報にする
def dropPast(g, mustdelete=None):
    while Grand[g]:
        minusrate, child = Grand[g][0]
        if Nowin[child] != g or child == mustdelete:
            hp.heappop(Grand[g])
        else:
            break


for c, d in CD:
    rate = AB[c-1][0]
    grandbefore = Nowin[c]
    # 過去の情報を捨てる
    dropPast(grandbefore)
    
    minusrate, child = Grand[grandbefore][0]
    # 現在トップがcなら変更あり
    if child == c:
        Bit.delete(-minusrate) # 移動するので消す
        hp.heappop(Grand[grandbefore])
        dropPast(grandbefore, c)
        # 残ってるヤツの中で最大があるなら更新
        if Grand[grandbefore]:
            minusrate, child = Grand[grandbefore][0]
            Bit.push(-minusrate)

    dropPast(d)
    # 移動先に元々いる
    if Grand[d]:
        minusrate, child = Grand[d][0]
        # もし最大値が更新されるなら入れ替える
        if -minusrate < rate:
            Bit.delete(-minusrate)
            Bit.push(rate)
    # いない
    else:
        Bit.push(rate)

    Nowin[c] = d
    hp.heappush(Grand[d], (-rate, c))
    
    #print(Grand)
    #print(Bit)

    print(Bit[0])