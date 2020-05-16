import sys
input = sys.stdin.readline
import heapq as hp

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    l, r, c = map(int, input().split())
    graph[l-1].append((c, r-1))

for i in range(N-1):
    graph[i+1].append((0, i))

INF = 10**16
D = [INF for _ in range(N)] # 頂点iへの最短距離がD[i]
D[0] = 0 
q = [] # しまっていく優先度付きキュー
hp.heappush(q, (0, 0))

while q:
    nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
    if D[np] < nd: # 追加した後の残骸は見ない
        continue
    for d, p in graph[np]:
        if D[p] > D[np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
            D[p] = D[np] + d
            hp.heappush(q, (D[p], p))

d = D[-1]
if d == INF:
    print(-1)
else:
    print(d)