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

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRX = [list(map(int, input().split())) for _ in range(Q)]

Co = {-1}
for a in A:
    Co.add(a)
for L, R, X in LRX:
    Co.add(X)
    Co.add(L)
    Co.add(R)

ind_to_co = sorted(list(Co))
co_to_ind = {}
for i, c in enumerate(ind_to_co):
    co_to_ind[c] = i

BIT = BITbisect(len(ind_to_co)+1)

for a in A:
    BIT.insert(co_to_ind[a])

for L, R, X in LRX:
    il = BIT.bisect_left(co_to_ind[L])
    ir = BIT.bisect_right(co_to_ind[R])

    bit = 0
    for _ in range(ir-il):
        b = ind_to_co[BIT.search(il)]
        bit ^= b
        BIT.delete(co_to_ind[b])
    
    print(bit)
    if (ir-il)%2 == 1:
        BIT.insert(co_to_ind[X])