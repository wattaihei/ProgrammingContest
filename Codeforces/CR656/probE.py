import sys
input = sys.stdin.buffer.readline

Q = int(input())
for _ in range(Q):
    N, M = map(int, input().split())
    graph = [set() for _ in range(N)]
    Indeg = [0]*N
    Edges = []
    De = []
    for _ in range(M):
        directed, a, b = map(int, input().split())
        if directed:
            graph[a-1].add(b-1)
            Indeg[b-1] += 1
            De.append((a-1, b-1))
        else:
            Edges.append((a-1, b-1))
    
    sortedEdges = []
    stack = []
    for n in range(N):
        if Indeg[n] == 0:
            stack.append(n)
    
    while stack:
        n = stack.pop()
        for v in graph[n]:
            Indeg[v] -= 1
            if Indeg[v] == 0: stack.append(v)
        sortedEdges.append(n)
    
    if len(sortedEdges) == N:
        print("YES")
        Seq = [-1]*N
        for i, n in enumerate(sortedEdges):
            Seq[n] = i
        for a, b in Edges:
            if Seq[a] > Seq[b]:
                a, b = b, a
            print(a+1, b+1)
        for a, b in De:
            print(a+1, b+1)
    else:
        print("NO")
