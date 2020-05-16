import sys
input = sys.stdin.readline

import heapq as hp

N, M, S, G = map(int, input().split())
graph_y = [[] for _ in range(N)]
graph_s = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    graph_y[a-1].append((c, b-1))
    graph_y[b-1].append((c, a-1))
    graph_s[a-1].append((d, b-1))
    graph_s[b-1].append((d, a-1))

INF = 10**18

def dijkstra(graph, s):
    D = [INF for _ in range(N)] # 頂点iへの最短距離がD[i]
    D[s] = 0 
    q = [] # しまっていく優先度付きキュー
    hp.heappush(q, (0, s))

    while q:
        nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
        if D[np] < nd: # 追加した後の残骸は見ない
            continue
        for d, p in graph[np]:
            if D[p] > D[np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
                D[p] = D[np] + d
                hp.heappush(q, (D[p], p))
    
    return D

Ds = dijkstra(graph_y, S-1)
Dg = dijkstra(graph_s, G-1)

ans = [None]*N
ans[N-1] = Ds[N-1] + Dg[N-1]
for n in reversed(range(N-1)):
    ans[n] = min(ans[n+1], Ds[n]+Dg[n])

for a in ans:
    print(10**15-a)