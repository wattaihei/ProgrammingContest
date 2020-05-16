N = int(input())
import sys
sys.setrecursionlimit(90000)

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

color = [-1 for _ in range(N)]
def dfs(p, c, color):
    color[p] = c
    cinv = 0 if c == 1 else 1
    for q, d in graph[p]:
        if color[q] != -1:
            continue
        if d % 2 == 1:
            color = dfs(q, cinv, color)
        else:
            color = dfs(q, c, color)
    return color

A = dfs(0, 0, color)
for a in A:
    print(a)