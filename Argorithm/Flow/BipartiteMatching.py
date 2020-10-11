# AOJ GRL_7_A "Bipartite Matching"
# O(VE)

class BipartiteMatching():
    def __init__(self, V1, V2):
        self.V1 = V1
        self.V2 = V2
        self.V = V1 + V2
        self.graph = [[] for _ in range(V1+V2)]
    
    def add_edge(self, v1, v2):
        v2 += self.V1
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    # search increasing path
    def dfs(self, s):
        self.par = [None]*self.V
        self.used = [False]*self.V
        self.used[s] = True
        self.stack = [s]
        while self.stack:
            v = self.stack.pop()
            for nv in self.graph[v]:
                w = self.match[nv]
                if w < 0:
                    while True:
                        self.match[v] = nv
                        self.match[nv] = v
                        if v == s: return True
                        v, nv = self.par[v]
                elif not self.used[w]:
                    self.par[w] = (v, nv)
                    self.used[w] = True
                    self.stack.append(w)
        return False

    def bipartite_matching(self):
        res = 0
        self.match = [-1]*self.V
        for v in range(self.V):
            if self.match[v] < 0:
                if self.dfs(v):
                    res += 1
        return res

"""
if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    V1, V2, E = map(int, input().split())
    bm = BipartiteMatching(V1, V2)
    for _ in range(E):
        a, b = map(int, input().split())
        bm.add_edge(a, b)
    print(bm.bipartite_matching())
"""