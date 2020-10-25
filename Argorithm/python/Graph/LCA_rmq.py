class LCA():
    def __init__(self, graph, rootNode=0):
        self.graph = graph
        self.N = len(graph)
        self.root = rootNode
    
        # DFS
        stack = [self.root]
        self.Depth = [-1]*self.N
        self.Parent = [-1]*self.N
        self.Depth[self.root] = 0
        self.Id = [-1]*self.N
        self.EulerTour = [0]*(2*self.N-1)
        for ind in range(2*self.N-1):
            p = stack.pop()
            if p >= 0:
                stack.append(~p)
                self.Id[p] = ind
                self.EulerTour[ind] = p
                for np in self.graph[p]:
                    if self.Depth[np] == -1:
                        self.Parent[np] = p
                        self.Depth[np] = self.Depth[p] + 1
                        stack.append(np)
            else:
                self.EulerTour[ind] = self.Parent[~p]
        
        # Sparse Table
        self.spN = len(self.EulerTour)
        self.splogN = self.spN.bit_length()
        self.A = [self.Depth[v] for v in self.EulerTour]
        self.table = [[0]*(self.spN-(1<<k)+1) for k in range(self.splogN+1)]
        self.table[0] = [i for i in range(self.spN)]
        for k in range(self.splogN):
            for i in range(self.spN-(1<<(k+1))+1):
                ind1 = self.table[k][i]
                ind2 = self.table[k][i+(1<<k)]
                if self.A[ind1] <= self.A[ind2]:
                    self.table[k+1][i] = ind1
                else:
                    self.table[k+1][i] = ind2

    # [l, r)のminの(val, key)
    def _query_min(self, l, r):
        k = (r-l).bit_length()-1
        indl = self.table[k][l]
        indr = self.table[k][r-(1<<k)]
        if self.A[indl] <= self.A[indr]:
            return indl
        return indr
    
    def LCAquery(self, u, v):
        idu = self.Id[u]
        idv = self.Id[v]
        if idu > idv:
            idu, idv = idv, idu
        lcaid = self._query_min(idu, idv+1)
        return self.EulerTour[lcaid]

    def distance(self, u, v):
        lca = self.LCAquery(u, v)
        return self.Depth[u] + self.Depth[v] - 2*self.Depth[lca]

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
        a -= 1; b -= 1
        print(lca.distance(a, b) + 1)
"""