import math
import heapq as hp
import sys
input = sys.stdin.readline

sx, sy, tx, ty = map(int, input().split())
N = int(input())
XYR = [list(map(int, input().split())) for _ in range(N)]
INF = 10**14

graph = [[] for _ in range(N+2)]
for i in range(N-1):
    for j in range(1, N):
        x1, y1, r1 = XYR[i]
        x2, y2, r2 = XYR[j]
        d = max(0, math.sqrt((x1-x2)**2+(y1-y2)**2)-r1-r2)
        graph[i].append((d, j))
        graph[j].append((d, i))

for i in range(N):
    x, y, r = XYR[i]
    graph[N].append((max(0, math.sqrt((x-sx)**2+(y-sy)**2)-r), i))
    graph[i].append((max(0, math.sqrt((x-tx)**2+(y-ty)**2)-r), N+1))

graph[N].append((math.sqrt((tx-sx)**2+(ty-sy)**2), N+1))

D = [INF for _ in range(N+2)] # 頂点iへの最短距離がD[i]
D[N] = 0 
q = [] # しまっていく優先度付きキュー
hp.heappush(q, (0, N))

while q:
    nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
    if D[np] < nd: # 追加した後の残骸は見ない
        continue
    for d, p in graph[np]:
        if D[p] > D[np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
            D[p] = D[np] + d
            hp.heappush(q, (D[p], p))

print(D[N+1])