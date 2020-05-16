# AOJ GRL_1_A Single Sourse Shortest Path
import heapq as hp
import sys
input = sys.stdin.readline

V, E, T = map(int, input().split())
A = list(map(int, input().split()))
graph1 = [[] for _ in range(V)]
graph2 = [[] for _ in range(V)]
INF = 10**14
for _ in range(E):
    a, b, d = map(int, input().split())
    graph1[a-1].append((d, b-1)) 
    graph2[b-1].append((d, a-1)) #無向グラフならこれ使う

def dijkstra(graph):
    D = [INF for _ in range(V)] # 頂点iへの最短距離がD[i]
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
    return D

def main():
    D1 = dijkstra(graph1)
    D2 = dijkstra(graph2)

    ans = 0
    for n in range(V):
        if D1[n] == INF or D2[n] == INF: continue
        t = T - D1[n] - D2[n]
        if t > 0:
            ans = max(ans, t*A[n])
    print(ans)


if __name__ == "__main__":
    main()