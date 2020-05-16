import sys
input = sys.stdin.readline

# 二部探索木の代わり
# max_Xが大きい場合、0を含む場合は座標圧縮する

class BITbisect():
    def __init__(self, max_X):
        self.max_X = max_X + 1
        self.bit = [0]*(self.max_X+1)

    # x番目にaを加える
    def add(self, x, a):
        while x <= self.max_X:
            self.bit[x] += a
            x += x & -x

    def insert(self, x):
        self.add(x, 1)

    def delete(self, x):
        self.add(x, -1)

    # xまでに出現している個数
    def query_sum(self, x):
        s = 0
        while x > 0:
            s += self.bit[x]
            x -= x & -x
        return s

    def exist(self, x):
        if self.query_sum(x) - self.query_sum(x-1) > 0:
            return True
        return False
    
    def count(self, x):
        return self.query_sum(x) - self.query_sum(x-1)

    # xより大きくてbitに入ってるもののうち最小のもの
    # O((logN)^2)
    def upper(self, x):
        qx = self.query_sum(x) + 1
        if qx > self.query_sum(self.max_X):
            return False
        l = 0
        r = self.max_X
        while l < r:
            m = (l+r)//2
            if self.query_sum(m) < qx:
                if l == m:
                    return r
                l = m
            else:
                r = m
        if m == self.max_X:
            return False
        return m

    # x以下でbitに入っているもののうち最大のもの
    # O((logN)^2)
    def lower(self, x):
        qx = self.query_sum(x)
        if qx == 0:
            return False
        l = 0
        r = self.max_X
        while r-l > 1:
            m = (l+r)//2
            if self.query_sum(m) < qx:
                l = m
            else:
                r = m
        if l == 0:
            return False
        return l

    # listみたいに表示
    def display(self):
        print('inside BIT:', end=' ')
        for x in range(1, self.max_X):
            if bit.exist(x):
                c = bit.count(x)
                for _ in range(c):
                    print(x, end=' ')
        print()

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    bit = BITbisect(N+1)
    for i in range(K):
        bit.insert(P[i]+1)
    c = 0
    for j in range(N-K):
        if bit.lower(P[j]+1) is False and bit.upper(P[j+K]+1) is False:
            c += 1
        bit.delete(P[j]+1)
        bit.insert(P[j+K]+1)


    k = -1
    l = 0
    same = 0
    for i in range(N):
        if P[i] > k:
            l += 1
        else:
            l = 1
        k = P[i]
        if l >= K:
            same += 1

    print(N-K+1-c-max(0, same-1))

if __name__ == "__main__":
    main()