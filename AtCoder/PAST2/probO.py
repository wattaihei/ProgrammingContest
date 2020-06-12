# verified: ABC014-D
# calculate LCA O(logN) for each query

# kprev[k][i]: 2^k parent of node i 
# if there is no node returns "None"
# Depth[i]: Depth of node i from rootNode

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

class Doubling():
    def __init__(self, graph, rootNode=0):
        self.graph = graph
        self.N = len(graph)
        self.Log_N = (self.N-1).bit_length()
        self.rootNode = rootNode
        # BFS
        self.prev = [None]*self.N
        self.pmax = [0]*self.N
   
        self.Depth = [-1]*self.N
        q = [self.rootNode]
        self.Depth[self.rootNode] = 0
        d = 0
        while q:
            qq = []
            d += 1
            for p in q:
                for np, a in self.graph[p]:
                    if self.Depth[np] == -1:
                        self.pmax[np] = a
                        self.prev[np] = p
                        self.Depth[np] = d
                        qq.append(np)
            q = qq

        # construct
        self.kprev = [self.prev]
        self.pkprev = [self.pmax]
        S = self.prev
        U = self.pmax
        for k in range(self.Log_N):
            T = [None]*self.N
            W = [0]*self.N
            for i in range(self.N):
                if S[i] is None:
                    continue
                T[i] = S[S[i]]
                W[i] = max(U[i], U[S[i]])
            self.kprev.append(T)
            S = T
            self.pkprev.append(W)
            U = W

    # LCA
    def query(self, u, v):
        dd = self.Depth[v] - self.Depth[u]
        if dd < 0:
            u, v = v, u
            dd = -dd
        
        # set same Depth
        ret_max = 0
        for k in range(self.Log_N+1):
            if dd & 1:
                ret_max = max(ret_max, self.pkprev[k][v])
                v = self.kprev[k][v]
            dd >>= 1
        
        if u == v:
            return ret_max
        
        for k in reversed(range(self.Log_N)):
            pu = self.kprev[k][u]
            pv = self.kprev[k][v]
            if pu != pv:
                ret_max = max(ret_max, self.pkprev[k][u])
                ret_max = max(ret_max, self.pkprev[k][v])
                u, v = pu, pv
        ret_max = max(ret_max, self.pkprev[0][u])
        ret_max = max(ret_max, self.pkprev[0][v])
        return ret_max
    



import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    Edges.append((c, a-1, b-1, i))

uni = UnionFind(N)

Edges.sort()
Tree = [[] for _ in range(N)]
TreeEdges = []
Undefined = []
Weight = 0
for c, a, b, i in Edges:
    if uni.isSameGroup(a, b):
        Undefined.append((c, a, b, i))
    else:
        uni.Unite(a, b)
        Weight += c
        Tree[a].append((b, c))
        Tree[b].append((a, c))
        TreeEdges.append(i)

ans = [0]*M

for i in TreeEdges:
    ans[i] = Weight

double = Doubling(Tree)
for (c, a, b, i) in Undefined:
    m = double.query(a, b)
    ans[i] = Weight - m + c

print(*ans, sep="\n")