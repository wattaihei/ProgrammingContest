class UnionFind():
    # 作りたい要素数nで初期化
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズ
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M, a, b = map(int, input().split())
    CD = [list(map(int, input().split())) for _ in range(M)]
    Query.append((N, M, a, b, CD))


def main():
    for N, M, a, b, CD in Query:
        uni1 = UnionFind(N)
        uni2 = UnionFind(N)
        for c, d in CD:
            if c != a and d != a:
                uni1.Unite(c, d)
            if c != b and d != b:
                uni2.Unite(c, d)
        p0 = 0
        p1 = 0
        for n in range(1, N+1):
            if uni1.isSameGroup(n, b) and not uni2.isSameGroup(n, a):
                p0 += 1
            if not uni1.isSameGroup(n, b) and uni2.isSameGroup(n, a):
                p1 += 1
        print((p0-1)*(p1-1))


if __name__ == "__main__":
    main()