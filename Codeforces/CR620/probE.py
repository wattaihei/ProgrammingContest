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
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

Q = int(input())
Query = []
for _ in range(Q):
    x, y, a, b, k = map(int, input().split())
    Query.append((x-1, y-1, a-1, b-1, k))

doubling = Doubling(graph)

def solve(x, y, a, b, k):
    d_a = doubling.Depth[a]
    d_b = doubling.Depth[b]
    d_x = doubling.Depth[x]
    d_y = doubling.Depth[y]

    lca_ab = doubling.LCAquery(a, b)
    d_ab = d_a + d_b - 2*doubling.Depth[lca_ab]
    
    lca_ax = doubling.LCAquery(a, x)
    d_ax = d_x + d_a - 2*doubling.Depth[lca_ax]

    lca_yb = doubling.LCAquery(y, b)
    d_yb = d_y + d_b - 2*doubling.Depth[lca_yb]

    lca_ay = doubling.LCAquery(a, y)
    d_ay = d_y + d_a - 2*doubling.Depth[lca_ay]

    lca_xb = doubling.LCAquery(x, b)
    d_xb = d_x + d_b - 2*doubling.Depth[lca_xb]

    Ds = [d_ab, d_ax + d_yb + 1, d_ay + d_xb + 1]
    for d in Ds:
        if d <= k and (k-d)%2 == 0:
            return True
    return False
    


for x, y, a, b, k in Query:
    ok = solve(x, y, a, b, k)
    print("YES" if ok else "NO")