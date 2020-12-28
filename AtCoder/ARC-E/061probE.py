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
from collections import deque

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N)]
Edges = []
for i in range(M):
    p, q, c = map(int, input().rstrip().split())
    graph[p-1].append((q-1, c))
    graph[q-1].append((p-1, c))
    Edges.append((p-1, q-1, c))

uni = UnionFind(M)
# dic[(node, color)] = number of root vertice
dic = {}
for i, (p, q, c) in enumerate(Edges):
    if (p, c) in dic:
        uni.Unite(dic[(p, c)], i)
    else:
        dic[(p, c)] = i
    if (q, c) in dic:
        uni.Unite(dic[(q, c)], i)
    else:
        dic[(q, c)] = i

edgeToPoint = {}
for (p, c), i in dic.items():
    r = uni.Find_Root(i)
    if r in edgeToPoint:
        edgeToPoint[r].append(p)
    else:
        edgeToPoint[r] = [p]

D = [-1]*N
Dm = [-1]*M
q = deque()
q.append(0)
D[0] = 0

while q:
    p = q.pop()
    if p >= 0:
        for np, c in graph[p]:
            m = uni.Find_Root(dic[(p, c)])
            if Dm[m] == -1:
                Dm[m] = D[p] + 1
                q.appendleft(~m)
    else:
        m = ~p
        for np in edgeToPoint[m]:
            if D[np] == -1:
                D[np] = Dm[m]
                q.append(np)

print(D[N-1])