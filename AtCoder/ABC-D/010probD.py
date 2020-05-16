# AOJ GRL_6_A "Maximum Flow"
# Ford-Fulkerson method

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# can run flow c from u to v (0-indexed)
# edge = {going vertice, capacity, index of reverse edge}
V, G, E = map(int, input().split())
V += 1
P = list(map(int, input().split()))
graph = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append([v, 1, len(graph[v])])
    graph[v].append([u, 0, len(graph[u])-1])
    graph[v].append([u, 1, len(graph[u])])
    graph[u].append([v, 0, len(graph[v])-1])

INF = 10**12
start = 0
finish = V-1
for p in P:
    graph[p].append([finish, 1, len(graph[finish])])
    graph[finish].append([p, 0, len(graph[p])-1])

used = [False]*V

# search increasing path
# v: vertice
def dfs(v, finish, flow):
    if v == finish: return flow
    used[v] = True
    for i, (nv, ncap, nrev) in enumerate(graph[v]):
        if not used[nv] and ncap > 0:
            d = dfs(nv, finish, min(flow, ncap))
            # run flow over reverse edge if can
            if d > 0:
                graph[v][i][1] -= d
                graph[nv][nrev][1] += d
                return d
    return 0

# solve
def max_flow(start, finish):
    flow = 0
    while True:
        global used
        used = [False]*V
        f = dfs(start, finish, INF)
        if f == 0: return flow
        flow += f


if __name__ == "__main__":
    print(max_flow(start, finish))