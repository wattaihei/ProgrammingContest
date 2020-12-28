import sys
input = sys.stdin.buffer.readline

INF = 10**18

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

def solve(N, A):
    A = [0] + A
    updated = True
    while updated:
        updated = False
        for i in reversed(range(1, N+1)):
            s = 0
            for j in range(i, N+1, i):
                s += A[j]
            if s < 0:
                updated = True
                for j in range(i, N+1, i):
                    A[j] = 0
    return sum(A)

def solve2(N, A):
    ans = 0
    for bit in range(1<<N):
        to_del = set()
        for i in range(N):
            if bit&(1<<i):
                for j in range(i, N, i+1):
                    to_del.add(j)
        s = 0
        for i in range(N):
            if not i in to_del:
                s += A[i]
        if s > ans:
            ans = s
    return ans

def solve3(N, A):
    fl = MinimumCostFlow(N+1)
    for i in range(N):
        for j in range(i, N, i+1):
            fl.add_edge(i, j, INF, 0)
        fl.add_edge(i, N, 1, A[i])
    mincost = fl.min_cost_flow(0, N, 0)
    return sum(A) - mincost
    

def count():
    import matplotlib.pyplot as plt
    Ns = []
    P = []
    for n in range(20):
        Bs = set()
        for bit in range(1<<n):
            for i in range(n):
                if bit&(1<<i):
                    for j in range(i, n, i+1):
                        bit |= (1<<j)
            Bs.add(bit)
        Ns.append(n)
        P.append(len(Bs))
        print(n, len(Bs))

    plt.plot(Ns, P)
    # plt.xscale("log")
    plt.yscale("log")
    plt.show()

# N = int(input())
# A = list(map(int, input().rstrip().split()))
# N = 10
# A = [7, -5, -9, -6, -2, -10, 6, 6, 7, 4]

# print(solve2(N, A))
# print(solve(N, A))

count()

# import random

# while True:
#     N = 10
#     A = [random.randint(-10, 10) for _ in range(N)]

#     ans2 = solve3(N, A)
#     ans1 = solve(N, A)
    
#     if ans1 != ans2:
#         print(N, A)
#         print(ans1, ans2)
#         break
