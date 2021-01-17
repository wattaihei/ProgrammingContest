# maximum flow
# O(EV^2)

class Dinic():
    def __init__(self, N, INF=10**18):
        self.INF = INF
        self.graph = [{} for _ in range(N)]
        self.N = N
        self.level = [-1]*N
    
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
    
    def construct(self):
        self.orderedgraph = [[] for _ in range(self.N)]
        for v in range(self.N):
            self.orderedgraph[v] = list(self.graph[v].keys())

    # make level
    def bfs(self, start):
        self.level = [-1]*self.N
        self.que = [start]
        self.level[start] = 0
        while self.que:
            qq = []
            for p in self.que:
                for np, ncap in self.graph[p].items():
                    if ncap > 0 and self.level[np] == -1:
                        self.level[np] = self.level[p] + 1
                        qq.append(np)
            self.que = qq

    def dfs(self, start, finish):
        self.Flow = [self.INF]*self.N
        self.iter = [0]*self.N
        self.Par = [-1]*self.N
        self.stack = [start]
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
            # for nv, ncap in self.graph[v].items():
            for i in range(self.iter[v], len(self.orderedgraph[v])):
                self.iter[v] = i
                nv = self.orderedgraph[v][i]; ncap = self.graph[v][nv]
                if ncap > 0 and self.level[v] < self.level[nv]:
                    self.stack.append(nv)
                    self.Par[nv] = v
                    self.Flow[nv] = min(self.Flow[v], ncap)
        return 0

    # solve
    def flow(self, start, finish):
        self.construct()
        flow = 0
        while True:
            self.bfs(start)
            if self.level[finish] < 0: return flow
            while True:
                f = self.dfs(start, finish)
                if f == 0: break
                flow += f


import sys
input = sys.stdin.buffer.readline

INF = 10**18

N = int(input())
A = list(map(int, input().rstrip().split()))

s = N
t = N+1

dinic = Dinic(N+2)
base = 0
for i, a in enumerate(A):
    if a > 0:
        base += a
        dinic.add_edge(i, t, a)
    else:
        dinic.add_edge(s, i, -a)
        for j in range(2*i+1, N, i+1):
            dinic.add_edge(i, j, INF)

c = dinic.flow(s, t)
print(base-c)