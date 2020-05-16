# AOJ GRL_1_A Single Sourse Shortest Path
import heapq as hp

V, E, s = map(int, input().split())
graph = [[] for _ in range(V)]
INF = 0
for _ in range(E):
    a, b, d = map(int, input().split())
    graph[a].append((d, b)) 
    #graph[b].append((d, a)) #無向グラフならこれ使う
    INF = max(INF, d)

INF = INF*(E+1) + 1
D = [INF for _ in range(V)] # 頂点iへの最短距離がD[i]
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

for d in D:
    if d == INF:
        print('INF')
    else:
        print(d)