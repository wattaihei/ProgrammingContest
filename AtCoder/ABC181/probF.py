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
input = sys.stdin.buffer.readline
from math import sqrt

N = int(input())
XY = [list(map(int, input().rstrip().split())) for _ in range(N)]

Distances = []
for i, (x1, y1) in enumerate(XY):
    for j in range(i+1, N):
        x2, y2 = XY[j]
        Distances.append((sqrt((x1-x2)**2 + (y1-y2)**2), i, j))
    Distances.append((100-y1, N, i))
    Distances.append((y1+100, N+1, i))
Distances.append((200, N, N+1))

Distances.sort()
uni = UnionFind(N+2)
cnt = N+2
ans = 0
for d, i, j in Distances:
    if cnt >= 2 and uni.Find_Root(N) != uni.Find_Root(N+1):
        ans = max(ans, d)
    r1 = uni.Find_Root(i)
    r2 = uni.Find_Root(j)
    if r1 != r2:
        cnt -= 1
        uni.Unite(r1, r2)


print(ans/2)
