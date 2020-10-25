# maximum flow
# O(F(V+E))

class FordFulkerson():
    def __init__(self, N, INF=10**18):
        self.INF = INF
        self.graph = [{} for _ in range(N)]
        self.N = N
    
    def add_edge(self, u, v, cap, undirected=False):
        # u -> v (maxflow: cap)
        if cap == 0: return
        if undirected:
            self.graph[u][v] = cap
            self.graph[v][u] = cap
        elif v in self.graph[u]:
            self.graph[u][v] = cap
        else:
            self.graph[u][v] = cap
            self.graph[v][u] = 0

    def dfs(self, start, finish):
        self.Flow = [self.INF]*self.N
        self.used = [False]*self.N
        self.Par = [-1]*self.N
        self.stack = [start]
        self.used[start] = True
        while self.stack:
            v = self.stack.pop()
            if v == finish:
                d = self.Flow[v]
                while v != start:
                    nv = self.Par[v]
                    self.graph[nv][v] -= d
                    self.graph[v][nv] += d # inverse edge
                    v = nv
                return d
            for nv, ncap in self.graph[v].items():
                if not self.used[nv] and ncap > 0:
                    self.used[nv] = True
                    self.stack.append(nv)
                    self.Par[nv] = v
                    self.Flow[nv] = min(self.Flow[v], ncap)
        return 0

    # solve
    def flow(self, start, finish):
        flow = 0
        while True:
            f = self.dfs(start, finish)
            if f == 0: return flow
            flow += f

"""
if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    ff = FordFulkerson(N)
    for _ in range(M):
        a, b, c = map(int, input().split())
        ff.add_edge(a, b, c)
    print(ff.flow(0, N-1))
"""