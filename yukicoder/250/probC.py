import heapq as hp
import sys
input = sys.stdin.readline

INF = 10**18

N, M = map(int, input().split())
X, Y = map(int, input().split())
X -= 1; Y -= 1
XY = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    x1, y1 = XY[a]; x2, y2 = XY[b]
    d = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    graph[a].append((d, b))
    graph[b].append((d, a))



D = [INF for _ in range(N)] # 頂点iへの最短距離がD[i]
D[X] = 0 
q = [] # しまっていく優先度付きキュー
hp.heappush(q, (0, X))

while q:
    nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
    if D[np] < nd: # 追加した後の残骸は見ない
        continue
    for d, p in graph[np]:
        if D[p] > D[np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
            D[p] = D[np] + d
            hp.heappush(q, (D[p], p))

print(D[Y])