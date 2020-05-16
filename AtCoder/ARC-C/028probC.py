import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N-1):
    a = int(input())
    graph[i+1].append(a)
    graph[a].append(i+1)

Ds = [[] for _ in range(N)]
checked = [False]*N

def dfs(p):
    checked[p] = True
    s = 1
    for np in graph[p]:
        if not checked[np]:
            nows = dfs(np)
            Ds[p].append(nows)
            Ds[np].append(N-nows)
            s += nows
    return s

dfs(0)
for n in range(N):
    print(max(Ds[n]))