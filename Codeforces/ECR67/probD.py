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

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Query.append((N, A, B))

for N, A, B in Query:
    bitA = BITbisect(N)
    bitB = BITbisect(N)
    ans = 'YES'
    for i in range(N):
        a, b = A[i], B[i]
        if bitA.length() == 0 and bitB.length() == 0:
            if a == b: continue
        if bitB.count(b) > 0:
            bitB.delete(b)
        else:
            bitA.insert(b)
        if bitA.count(a) > 0:
            bitA.delete(a)
        else:
            bitB.insert(a)
        #print(i)
        #bitA.display()
        #bitB.display()
        if bitA.length() != 0 or bitB.length() != 0:
            if i == N-1:
                ans = 'NO'
            elif B[i] > B[i+1]:
                ans = 'NO'
                break
                
    print(ans)