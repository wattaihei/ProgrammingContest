import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, x = map(int, input().split())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

x -= 1

checked = [False]*N

def dfs(p):
    checked[p] = True
    need = False
    s = 0
    for np in graph[p]:
        if not checked[np]:
            nextneed, nexts = dfs(np)
            need = need or nextneed
            s += nexts
    
    if need or A[p]:
        return True, s+1
    return False, 0

need, s = dfs(x)
if need:
    s -= 1
print(s*2)