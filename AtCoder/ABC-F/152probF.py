import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
Edges = [[None]*N for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    Edges[a-1][b-1] = i
    Edges[b-1][a-1] = i

def dfs(p, L, checked, goal):
    if p == goal:
        return L
    checked[p] = True
    ok = False
    for np in graph[p]:
        if not checked[np]:
            L.append(np)
            retL = dfs(np, L, checked, goal)
            if retL:
                ok = True
                break
            L.pop()
    if ok:
        return retL
    else:
        return []


M = int(input())
Compression = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    path = dfs(a, [], [False]*N, b)
    bit = 0
    pre = a
    for p in path:
        bit += 1<<Edges[pre][p]
        pre = p
    Compression.append(bit)

ans = 0
for bitmask in range(1,1<<M):
    whitebit = 0
    for i in range(M):
        if (1<<i)&bitmask:
            whitebit |= Compression[i]
    
    p = 1
    for n in range(M):
        if bitmask&(1<<n):
            p ^= 1
    E = 1
    for m in range(N-1):
        if whitebit&(1<<m) == 0:
            E *= 2
    
    ans += E*(-1)**p

print(2**(N-1)-ans)