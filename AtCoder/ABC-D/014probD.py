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

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
Pairs = [[] for _ in range(N)]
Q = int(input())
Query = []
for _ in range(Q):
    a, b = map(int, input().split())
    Pairs[a-1].append(b-1)
    Pairs[b-1].append(a-1)
    Query.append((a-1, b-1))

for n in range(N):
    if len(graph[n]) == 1:
        start = n
    
want_to_check = [[] for _ in range(N)]
UF = UnionFind(N)
root = {}
ans = {}
D = [-1]*N
d = 0
stack = [start]
while stack:
    p = stack[-1]

    if D[p] == -1:
        D[p] = d

        for pair in want_to_check[p]:
            if not UF.Find_Root(pair) in root.keys():
                dis = D[p] - D[pair]
            else:
                r = root[UF.Find_Root(pair)]
                dis = D[pair] + D[p] - 2*D[r]
            if not pair in ans.keys():
                ans[pair] = {p: dis}
            else:
                ans[pair][p] = dis
            if not p in ans.keys():
                ans[p] = {pair: dis}
            else:
                ans[p][pair] = dis

        for pair in Pairs[p]:
            if D[pair] == -1:
                want_to_check[pair].append(p)

    update = False
    for np in graph[p]:
        if D[np] == -1:
            update = True
            d += 1
            stack.append(np)
            break
    if not update:
        d -= 1
        stack.pop()
        if stack:
            UF.Unite(stack[-1], p)
            root[UF.Find_Root(p)] = stack[-1]

for a, b in Query:
    print(ans[a][b]+1)