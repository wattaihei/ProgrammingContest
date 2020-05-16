import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

checked = [False]*N
def dfs(p):
    checked[p] = True
    g = 0
    for np in graph[p]:
        if not checked[np]:
            g ^= dfs(np)+1
    return g

if dfs(0) == 0:
    print("Bob")
else:
    print("Alice")