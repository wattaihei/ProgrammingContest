import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(2, N+1):
    a = int(input())
    graph[a].append(i)


def dfs(p):
    if len(graph[p]) == 0:
        return 1
    gain = []
    for k in graph[p]:
        gain.append(dfs(k))
    return min(gain) + max(gain) + 1

print(dfs(1))