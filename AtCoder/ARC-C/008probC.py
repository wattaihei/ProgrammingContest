import sys
input = sys.stdin.readline
import heapq as hp
INF = 10**18
N = int(input())

def main1():
    Nodes = [list(map(int, input().split())) for _ in range(N)]

    graph = [[] for _ in range(N)]
    for i in range(N):
        x1, y1, t1, r1 = Nodes[i]
        for j in range(i+1, N):
            x2, y2, t2, r2 = Nodes[j]
            d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
            graph[i].append((j, d/min(t1, r2)))
            graph[j].append((i, d/min(r1, t2)))
    return graph

def main2():
    graph = main1()
    q = [(0, 0)]
    D = [INF]*N
    D[0] = 0
    while q:
        d, p = hp.heappop(q)
        if D[p] < d: continue
        for np, nd in graph[p]:
            if D[p] + nd < D[np]:
                D[np] = D[p] + nd
                hp.heappush(q, (D[np], np))
    return D


def main():
    D = main2()
    P = sorted(D[1:], reverse=True)
    ans = 0
    for i, p in enumerate(P):
        ans = max(ans, p+i)
    print(ans)


if __name__ == "__main__":
    main()