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
from bisect import bisect_left

N, M = map(int, input().split())
Edges = []
for i in range(M):
    u, v, c, w = map(str, input().split())
    if c == "0":
        Edges.append((int(u), int(v), int(w), 0))
    else:
        Edges.append((int(u), int(v), 0, 1))
Q = int(input())
Query = [int(input()) for _ in range(Q)]

Edges.sort(key=itemgetter(2))
U1 = UnionFind(N)
U2 = UnionFind(N)
count_x = 0
cost = 0
for u, v, w, is_x in Edges:
    if not U1.isSameGroup(u, v):
        U1.Unite(u, v)
        cost += w
        if not is_x:
            U2.Unite(u, v)
        else:
            count_x += 1


Count_x = [count_x]
Cost = [cost]
Edge_weights = []
for u, v, w, is_x in Edges:
    if is_x:
        continue
    if not U2.isSameGroup(u, v):
        U2.Unite(u, v)
        count_x -= 1
        cost += w
    Count_x.append(count_x)
    Cost.append(cost)
    Edge_weights.append(w)

for a in Query:
    i = bisect_left(Edge_weights, a)
    ans = a*Count_x[i] + Cost[i]
    print(ans)