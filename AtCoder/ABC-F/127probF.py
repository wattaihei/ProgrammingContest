# instead of AVLTree
class BITbisect():
    def __init__(self, max):
        self.max = max
        self.data = [0]*(self.max+1)
    
    # 0からiまでの区間和
    # 立っているビットを下から処理
    def query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    # i番目の要素にxを足す
    # 覆ってる区間すべてに足す
    def add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i

    def insert(self, x):
        self.add(x, 1)

    def delete(self, x):
        self.add(x, -1)

    def count(self, x):
        return self.query_sum(x) - self.query_sum(x-1)
    
    def length(self):
        return self.query_sum(self.max)
    
    # O(log(N))
    def search(self, c):
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1<<i) <= self.max:
                if s + self.data[ind+(1<<i)] < c:
                    s += self.data[ind+(1<<i)]
                    ind += (1<<i)
        return ind
    
    def bisect_right(self, x):
        return self.query_sum(x)

    def bisect_left(self, x):
        if x == 1:
            return 0
        return self.query_sum(x-1)

    # listみたいに表示
    def display(self):
        print('inside BIT:', end=' ')
        for x in range(1, self.max+1):
            if self.count(x):
                c = self.count(x)
                for _ in range(c):
                    print(x, end=' ')
        print()


import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

A = []
for i in range(Q):
    if Query[i][0] == 1:
        A.append(Query[i][1])

# 座標圧縮
ind_to_co = sorted(A)
co_to_ind = {}
for i, x in enumerate(ind_to_co):
    co_to_ind[x] = i+1

bit1 = BITbisect(Q+1) #傾き
bit2 = BITbisect(Q) #合計

b = 0
for q in range(Q):
    if Query[q][0] == 1:
        b += Query[q][2]
        a = Query[q][1]
        bit2.add(co_to_ind[a], a)
        bit1.add(1, -1)
        bit1.add(co_to_ind[a]+1, 2)
    else:
        i1 = bit1.search(0)
        a1 = ind_to_co[i1-1]
        #print(bit1.query_sum(i1), bit1.query_sum(1), bit1.query_sum(i1+1), bit1.query_sum(Q))
        delta = (bit1.query_sum(i1) - bit1.query_sum(1) + bit1.query_sum(i1+1) - bit1.query_sum(Q))//2
        a2 = bit2.query_sum(Q) - bit2.query_sum(i1-1) - bit2.query_sum(i1) + a1*delta + b
        print(a1, a2)
