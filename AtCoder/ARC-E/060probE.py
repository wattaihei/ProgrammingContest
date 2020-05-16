# verified: ABC014-D
# calculate LCA O(logN) for each query

# prev[i][k]: 2^k parent of node i 
# Depth[i]: Depth of node i from 0

class LCA():
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
    def query(self, u, v):
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

"""
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    lca = LCA(graph)
    for a, b in Query:
        r = lca.query(a-1, b-1)
        d = lca.Depth[a-1] + lca.Depth[b-1] - 2*lca.Depth[r]
        print(d+1)
"""

import sys
input = sys.stdin.readline
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
L = int(input())
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

graph = [[] for _ in range(N)]
for i, a in enumerate(A):
    j = bisect_right(A, a+L)-1
    graph[j].append(i)
    graph[i].append(j)


lca = LCA(graph, rootNode=N-1)
for a, b in Query:
    d = 0
    a -= 1; b-= 1
    if b < a:
        a, b = b, a
    for k in reversed(range(lca.Log_N)):
        nextnode = lca.kprev[k][a]
        if nextnode is None:
            continue
        else:
            if nextnode == b:
                d += 1<<k
                break
            elif A[nextnode] < A[b]:
                d += 1<<k
                a = nextnode
    if nextnode != b:
        d += 1
    print(d)