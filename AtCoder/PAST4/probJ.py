import sys
input = sys.stdin.readline

from heapq import heappop, heappush

INF = 10**18

N, M = map(int, input().rstrip().split())
xab, xac, xbc = map(int, input().rstrip().split())

def str_to_node(s):
    ABC = "ABC"
    return ABC.index(s) + N

S = list(input().rstrip())
graph = [[] for _ in range(N+3)]
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a-1].append((c, b-1))
    graph[b-1].append((c, a-1))

for i, s in enumerate(S):
    if s == "A":
        graph[i].append((xab, str_to_node("B")))
        graph[i].append((xac, str_to_node("C")))
        graph[str_to_node("A")].append((0, i))
    elif s == "B":
        graph[i].append((xab, str_to_node("A")))
        graph[i].append((xbc, str_to_node("C")))
        graph[str_to_node("B")].append((0, i))
    else:
        graph[i].append((xac, str_to_node("A")))
        graph[i].append((xbc, str_to_node("B")))
        graph[str_to_node("C")].append((0, i))

def dijkstra():
    q = [(0, 0)]
    D = [INF]*(N+3)
    D[0] = 0
    while q:
        d, p = heappop(q)
        if D[p] < d: continue
        for nd, np in graph[p]:
            if D[np] > D[p] + nd:
                D[np] = D[p] + nd
                heappush(q, (D[np], np))
    return D[N-1]

print(dijkstra())