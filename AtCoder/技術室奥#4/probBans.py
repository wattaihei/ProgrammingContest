import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M = map(int,input().split())
graph = [set() for _ in range(N+1)]
for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].add(y)
    graph[y].add(x)
C = set(int(x) for x in input().split())

# 次数1の頂点を縮約。端点が2点以下になっていればOK
print(graph)
deg = [len(x) for x in graph]
print(deg)
deg_1 = [i for i,x in enumerate(deg) if x == 1]
rest_deg_1 = []

while deg_1:
    print(deg_1)
    x = deg_1.pop()
    if x in C:
        rest_deg_1.append(x)
        continue
    y = graph[x].pop()
    graph[y].remove(x)
    deg[y] -= 1
    if deg[y] == 1:
        deg_1.append(y)
    

answer = 'Yes' if len(rest_deg_1) <= 2 else 'trumpet'
print(answer)
