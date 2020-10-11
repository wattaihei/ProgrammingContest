import heapq as hp
class MinimumCostFlow():
    def __init__(self, N, INF=10**18):
        self.graph = [{} for _ in range(N)]
        self.N = N
        self.INF = INF
    
    def add_edge(self, u, v, cap, cost, undirected=False):
        # u -> v (maxflow, cost)
        if cap == 0: return
        if undirected:
            self.graph[u][v] = [cap, cost]
            self.graph[v][u] = [cap, -cost]
        elif v in self.graph[u]:
            self.graph[u][v] = [cap, cost]
        else:
            self.graph[u][v] = [cap, cost]
            self.graph[v][u] = [0, -cost]       
    
    def dijkstra(self, start):
        self.dist = [self.INF]*self.N # nearest distance
        self.dist[start] = 0
        self.que = [(0, start)]
        while self.que:
            d, v = hp.heappop(self.que)
            if self.dist[v] < d: continue
            for nv, (ncap, ncost) in self.graph[v].items():
                if ncap > 0 and self.dist[nv] > self.dist[v] + ncost + self.H[v] - self.H[nv]:
                    self.dist[nv] = self.dist[v] + ncost + self.H[v] - self.H[nv]
                    self.prevv[nv] = v
                    hp.heappush(self.que, (self.dist[nv], nv))
                
    
    def min_cost_flow(self, start, finish, flow):
        self.res = 0
        self.prevv = [-1]*self.N
        self.H = [0]*self.N # potential
        while flow > 0:
            self.dijkstra(start)
            if self.dist[finish] == self.INF: return -1 # cant run flow anymore
            for i in range(self.N):
                self.H[i] += self.dist[i]
            
            d = flow
            v = finish
            while v != start:
                d = min(d, self.graph[self.prevv[v]][v][0])
                v = self.prevv[v]
            flow -= d
            self.res += d*self.H[finish]

            v = finish
            while v != start:
                self.graph[self.prevv[v]][v][0] -= d
                self.graph[v][self.prevv[v]][0] += d
                v = self.prevv[v]
        return self.res
    

INF = 10**5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = N*M
State = [list(input().rstrip()) for _ in range(N)]

FL = MinimumCostFlow(2*L+2)
c = 0
for n in range(N):
    for m in range(M):
        if State[n][m] == "o":
            FL.add_edge(2*L, m*N+n, 1, INF)
            c += 1
            cango = {(n-1, m)}
            for an in range(n, N):
                for am in range(m, M):
                    if ((an-1, am) in cango or (an, am-1) in cango) and State[an][am] != "#":
                        cango.add((an, am))
                        dist = an - n + am - m
                        FL.add_edge(m*N+n, L+am*N+an, 1, INF-dist)
        if State[n][m] != "#":
            FL.add_edge(m*N+n+L, 2*L+1, 1, INF)

ans = 3*c*INF - FL.min_cost_flow(2*L, 2*L+1, c)
print(ans)
