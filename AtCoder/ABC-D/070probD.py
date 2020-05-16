import heapq as hp

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    graph[a-1].append((d, b-1))
    graph[b-1].append((d, a-1))

Q, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(Q)]

INF = int(1E17)

D = [INF for _ in range(N)] # 頂点iへの最短距離がD[i]
D[K-1] = 0 
q = [] # しまっていく優先度付きキュー
hp.heappush(q, (0, K-1))

while q:
    nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
    if D[np] < nd: # 追加した後の残骸は見ない
        continue
    for d, p in graph[np]:
        if D[p] > D[np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
            D[p] = D[np] + d
            hp.heappush(q, (D[p], p))

for x, y in XY:
    print(D[x-1]+D[y-1])
