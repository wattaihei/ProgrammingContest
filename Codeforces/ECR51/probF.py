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

def main():
    import sys
    input = sys.stdin.readline
    import heapq as hp

    INF = 10**17

    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a-1].append((w, b-1))
        graph[b-1].append((w, a-1))


    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    tree_graph = [set() for _ in range(N)]
    Ex_Edges = set()
    q = [0]
    D = [-1]*N
    D[0] = 0
    while q:
        qq = []
        for p in q:
            for w, np in graph[p]:
                if D[np] == -1:
                    D[np] = D[p] + w
                    tree_graph[p].add(np)
                    tree_graph[np].add(p)
                    qq.append(np)
                elif not np in graph[p]:
                    Ex_Edges.add((min(np, p), max(np, p)))
        q = qq



    lca = LCA(tree_graph)



    def dijkstra(s):
        D1 = [INF]*N
        D1[s] = 0
        q = [(0, s)]
        while q:
            d, p = hp.heappop(q)
            if D1[p] < d: continue
            for nd, np in graph[p]:
                if D1[np] > D1[p] + nd:
                    D1[np] = D1[p] + nd
                    hp.heappush(q, (D1[np], np))
        return D1


    def distance(u, v):
        par = lca.LCAquery(u, v)
        return D[u] + D[v] - 2*D[par]


    Ds = []
    for u, v in Ex_Edges:
        Ds.append((dijkstra(u)))


    for a, b in Query:
        a -= 1; b -= 1
        ans = distance(a, b)
        for D1 in Ds:
            ans = min(ans, D1[a]+D1[b])
        print(ans)


if __name__ == "__main__":
    main()