import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    graph = [[] for _ in range(2*N)]
    Edges = []
    for _ in range(2*N-1):
        a, b, d = map(int, input().split())
        graph[a-1].append((b-1, d))
        graph[b-1].append((a-1, d))
        Edges.append((a-1, b-1, d))
    Query.append((N, graph))

for N, graph in Query:
    a0 = 0
    a1 = 0
    for a, b, d in Edges:
        if len(graph[a]) % 2 != 0 or len(graph[b]) % 2 != 0:
            a0 += d
    