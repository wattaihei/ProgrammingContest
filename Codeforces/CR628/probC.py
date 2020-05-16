import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
Edges = {}
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)
    Edges[str(a) + "," + str(b)] = i
    Edges[str(b) + "," + str(a)] = i

ans = [-1]*(N-1)
ind = 0
for n in range(N):
    if len(graph[n]) >= 3:
        for np in graph[n]:
            e = Edges[str(n) + "," + str(np)]
            ans[e] = ind
            ind += 1
            if ind >= 3:
                break
        break

for n in range(N-1):
    if ans[n] == -1:
        ans[n] = ind
        ind += 1

print(*ans, sep="\n")
        