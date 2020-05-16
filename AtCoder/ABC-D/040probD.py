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
ABY = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
VW = [[i] + list(map(int, input().split())) for i in range(Q)]

ABY.sort(reverse=True, key=itemgetter(2))
VW.sort(reverse=True, key=itemgetter(2))

ans = [0]*Q
ia = 0
ib = 0
uni = UnionFind(N)
while ib < Q:
    ind, v, w = VW[ib]
    if ia == M:
        ans[ind] = uni.Count(v)
        ib += 1
    else:
        a, b, y = ABY[ia]
        if w >= y:
            ans[ind] = uni.Count(v)
            ib += 1
        else:
            uni.Unite(a, b)
            ia += 1

for a in ans:
    print(a)