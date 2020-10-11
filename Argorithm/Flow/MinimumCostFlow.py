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
    
"""
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    V, E, F = map(int, input().split())
    fl = MinimumCostFlow(V)
    for _ in range(E):
        u, v, c, d = map(int, input().split())
        fl.add_edge(u, v, c, d)
    
    print(fl.min_cost_flow(0, V-1, F))
"""