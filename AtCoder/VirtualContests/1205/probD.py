import sys
input = sys.stdin.readline

# AOJ GRL_1_A Single Sourse Shortest Path
import heapq as hp

V, E = map(int, input().split())
Edges = []
P = []
INF = 10**16
for _ in range(E):
    a, b, d = map(int, input().split())
    if a == 1:
        P.append(b-1)
    elif b == 1:
        P.append(a-1)
    a, b = sorted([a, b])
    Edges.append((a-1, b-1, d))


def dijkstra(graph, p):
    D = [INF for _ in range(V)] # 頂点iへの最短距離がD[i]
    D[p] = 0 
    q = [] # しまっていく優先度付きキュー
    hp.heappush(q, (0, p))

    while q:
        nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
        if D[np] < nd: # 追加した後の残骸は見ない
            continue
        for d, p in graph[np]:
            if D[p] > D[np] + d: # 隣接するやつの中で今よりも近くなれるなら更新
                D[p] = D[np] + d
                hp.heappush(q, (D[p], p))
    
    return D[0]

def main():
    ans = INF
    for p in P:
        graph = [[] for _ in range(V)]
        for a, b, d in Edges:
            if a == 0:
                if b == p:
                    dis = d
                elif b != p:
                    graph[b].append((d, a))
            else:
                graph[a].append((d, b))
                graph[b].append((d, a))
        dis += dijkstra(graph, p)
        ans = min(ans, dis)

    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()