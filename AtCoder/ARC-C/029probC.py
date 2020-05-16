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
from operator import itemgetter

N, M = map(int, input().split())
Cost = [int(input()) for _ in range(N)]
Edges = [list(map(int, input().split())) for _ in range(M)]

Edges.sort(key=itemgetter(2))

uni = UnionFind(N)
ans = sum(Cost)
for a, b, w in Edges:
    a -= 1; b -= 1
    if uni.isSameGroup(a, b): continue
    r1 = Cost[uni.Find_Root(a)]
    r2 = Cost[uni.Find_Root(b)]
    if r1 < r2 and w <= r2:
        uni.Unite(a, b)
        ans += w - r2
        Cost[uni.Find_Root(a)] = r1
    if r2 <= r1 and w <= r1:
        uni.Unite(a, b)
        ans += w - r1
        Cost[uni.Find_Root(a)] = r2
print(ans)
        
