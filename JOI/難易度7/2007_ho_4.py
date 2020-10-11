import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
Nodes = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    Nodes[b-1] += 1

def topologicalSort(graph, Nodes, rev):
    stack = []
    for n in range(N):
        if Nodes[n] == 0: stack.append(n)
    if rev:
        stack = stack[::-1]

    TopologicalSort = []
    while stack:
        p = stack.pop()
        TopologicalSort.append(p)
        Nexts = graph[p] if not rev else reversed(graph[p])
        for np in Nexts:
            Nodes[np] -= 1
            if Nodes[np] == 0: stack.append(np)

    return TopologicalSort


T1 = topologicalSort(graph, Nodes[:], rev=False)
T2 = topologicalSort(graph, Nodes[:], rev=True)
for t in T1:
    print(t+1)
print(1 if T1 != T2 else 0)