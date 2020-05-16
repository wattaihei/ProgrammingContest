import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

checked = [False]*N
C = [None]*N
checked[0] = True

def dfs(p, c1, c2, depth):
    C[p] = c1 + c2
    d = 0
    for np in graph[p]:
        if not checked[np]:
            checked[np] = True
            d += 1
            g = 1 if depth > 0 else 0
            dfs(np, d, g, depth+1)
        

dfs(0, 0, 0, 0)
#print(C)

mod = 10**9+7
ans = 1
for n in range(N):
    ans = ans * (K-C[n]) % mod

print(ans)