# verified: ABC014-D
# calculate LCA O(logN) for each query

# kprev[k][i]: 2^k parent of node i 
# if there is no node returns "None"
# Depth[i]: Depth of node i from rootNode

class Doubling():
    def __init__(self, graph, rootNode=0):
        self.graph = graph
        self.N = len(graph)
        self.Log_N = (self.N-1).bit_length()
        self.rootNode = rootNode
        # self.Color = [-1]*self.N
        # BFS
        self.prev = [None]*self.N
   
        self.Depth = [-1]*self.N
        q = [self.rootNode]
        self.Depth[self.rootNode] = 0
        d = 0
        while q:
            qq = []
            d += 1
            for p in q:
                for np in self.graph[p]:
                    if self.Depth[np] == -1:
                        self.prev[np] = p
                        self.Depth[np] = d
                        qq.append(np)
            q = qq

        # construct
        self.kprev = [self.prev]
        S = self.prev
        for k in range(self.Log_N):
            T = [None]*self.N
            for i in range(self.N):
                if S[i] is None:
                    continue
                T[i] = S[S[i]]
            self.kprev.append(T)
            S = T

    # LCA
    def LCAquery(self, u, v):
        dd = self.Depth[v] - self.Depth[u]
        swapped = False
        if dd < 0:
            swapped = True
            u, v = v, u
            dd = -dd
        
        # set same Depth
        if dd > 0:
            dd -= 1
            for k in range(self.Log_N+1):
                if dd & 1:
                    v = self.kprev[k][v]
                dd >>= 1
        
            if u == self.kprev[0][v]:
                return (-1, v) if not swapped else (v, -1)
            v = self.kprev[0][v]
        
        for k in reversed(range(self.Log_N)):
            pu = self.kprev[k][u]
            pv = self.kprev[k][v]
            if pu != pv:
                u, v = pu, pv
        
        return (u, v) if not swapped else (v, u)
        # return self.kprev[0][u]

    def coloring(self, u, v, c):
        r = self.LCAquery(u, v)
        while u != r and self.Color[u] == -1:
            self.Color[u] = c
            u = self.kprev[0][u]
        while v != r and self.Color[v] == -1:
            self.Color[v] = c
            v = self.kprev[0][v]
    
    def deeper(self, u, v):
        if self.Depth[u] > self.Depth[v]:
            return u
        else:
            return v


import sys
input = sys.stdin.buffer.readline
from heapq import heappop, heappush

N, Q = map(int, input().rstrip().split())
graph = [[] for _ in range(N)]
Edges = []
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    Edges.append((a-1, b-1))

lca = Doubling(graph)
NodeInfo = [[] for _ in range(N)]
Query = [list(map(int, input().rstrip().split())) for _ in range(Q)]
for i, (u, v, c) in enumerate(Query):
    u -= 1; v -= 1
    pu, pv = lca.LCAquery(u, v)
    if pu != -1:
        NodeInfo[u].append((-i, c, pu))
    if pv != -1:
        NodeInfo[v].append((-i, c, pv))

q = []
stack = [0]
Color = [0]*N
checked = [False]*N
while stack:
    p = stack.pop()
    if p >= 0:
        stack.append(~p)
        for np in graph[p]:
            if np != lca.kprev[0][p]:
                stack.append(np)
    else:
        p = ~p
        # checked[p] = True
        for T in NodeInfo[p]:
            heappush(q, T)
        while q and checked[q[0][2]]:
            heappop(q)
        if q:
            Color[p] = q[0][1]
        checked[p] = True


for u, v in Edges:
    d = lca.deeper(u, v)
    print(Color[d])