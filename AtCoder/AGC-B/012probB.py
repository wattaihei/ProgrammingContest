import sys
input = sys.stdin.readline

INF = 10**14

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

maxd = 0
Q = int(input())
Query = []
Color = []
for _ in range(Q):
    v, d, c = map(int, input().split())
    if d > maxd:
        maxd = d
    Query.append((v-1, d))
    Color.append(c)

Query = Query[::-1]
Color = Color[::-1]

dp = [[INF]*(maxd+1) for _ in range(N)]
for i, (v, d) in enumerate(Query):
    if i < dp[v][d]:
        dp[v][d] = i

for d in reversed(range(maxd)):
    for v in range(N):
        if dp[v][d+1] < dp[v][d]:
            dp[v][d] = dp[v][d+1]
        for nv in graph[v]:
            if dp[v][d+1] < dp[nv][d]:
                dp[nv][d] = dp[v][d+1]

for v in range(N):
    seq = dp[v][0]
    if seq == INF:
        print(0)
    else:
        print(Color[seq])