import sys
input = sys.stdin.buffer.readline


Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
    Query.append((N, M, graph))

for N, M, graph in Query:
    Delete = [False]*N
    Seq = [0]*N
    for i in range(N):
        if Seq[i] >= 2:
            Delete[i] = True
            Seq[i] = -1
        for p in graph[i]:
            Seq[p] = max(Seq[i] + 1, Seq[p])
    ans = []
    for i in range(N):
        if Delete[i]:
            ans.append(i+1)
    print(len(ans))
    print(*ans)