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
    
    # 下からc番目(0-indexed)の数
    # O(log(N))
    def search(self, c):
        c += 1
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1<<i) <= self.max:
                if s + self.data[ind+(1<<i)] < c:
                    s += self.data[ind+(1<<i)]
                    ind += (1<<i)
        if ind == self.max:
            return False
        return ind + 1
    
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
from bisect import bisect_right

N = int(input())
A = []
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    AB.append((a, b))

sA = sorted(list(set(A)))
co_to_ind = {}
ind_to_co = [0]
for i, a in enumerate(sA):
    co_to_ind[a] = i+1
    ind_to_co.append(a)



def check(k):
    #print(k)
    bit = BITbisect(N+1)
    for a in A:
        bit.insert(co_to_ind[a])
    A_to_B = {}
    for a, b in AB:
        if not a in A_to_B:
            A_to_B[a] = [b]
        else:
            A_to_B[a].append(b)
    for _ in range(N):
        #bit.display()
        ind = bisect_right(ind_to_co, k)
        p = bit.bisect_left(ind)-1
        #print(ind, p, k)
        if p == -1:
            return False
        val = bit.search(p)
        a = ind_to_co[val]
        b = A_to_B[a].pop()
        k += b-a
        bit.delete(val)
    return True

l = 0
r = 10**14
while r-l > 1:
    m = (l+r)//2
    if check(m):
        r = m
    else:
        l = m

print(r)

