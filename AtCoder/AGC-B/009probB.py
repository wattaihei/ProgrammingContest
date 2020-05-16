import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
for n in range(1, N):
    a = int(input()) - 1
    graph[a].append(n)


def dfs(p):
    Ds = []
    for np in graph[p]:
        Ds.append(dfs(np))
    if not Ds:
        return 0
    l = len(Ds)
    Ds.sort(reverse=True)
    for i in range(l):
        Ds[i] += i+1
    return max(Ds)

ans = dfs(0)
print(ans)