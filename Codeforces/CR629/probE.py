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
        if dd < 0:
            u, v = v, u
            dd = -dd
        
        # set same Depth
        for k in range(self.Log_N+1):
            if dd & 1:
                v = self.kprev[k][v]
            dd >>= 1
        
        if u == v:
            return u
        
        for k in reversed(range(self.Log_N)):
            pu = self.kprev[k][u]
            pv = self.kprev[k][v]
            if pu != pv:
                u, v = pu, pv
        
        return self.kprev[0][u]

import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
Query = [list(map(int, input().split())) for _ in range(M)]


lca = Doubling(graph)

for A in Query:
    N = A[0]
    node = 0
    ok = True
    for a in A[1:]:
        a -= 1
        an = lca.LCAquery(a, node)
        if an != node and lca.Depth[a] - lca.Depth[an] > 1:
            ok = False
            break
        else:
            if a != 0 and lca.Depth[a] > lca.Depth[node]:
                node = lca.prev[a]
    print("YES" if ok else "NO")