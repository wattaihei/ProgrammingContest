import sys
input = sys.stdin.readline

INF = 10**17

V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[b-1].append(a-1) 

K = int(input())
A = list(map(int, input().split()))
g = A[-1] - 1

D = [INF for _ in range(V)] # 頂点iへの最短距離がD[i]
D[g] = 0 

q = [g]
while q:
    qq = []
    for p in q:
        for np in graph[p]:
            if D[np] == INF:
                D[np] = D[p] + 1
                qq.append(np)
    q = qq

Way = [set() for _ in range(V)]
for p in range(V):
    for np in graph[p]:
        if D[np] == D[p] + 1:
            Way[np].add(p)

a1 = 0
a2 = 0
for i in range(K-1):
    a = A[i]; b = A[i+1]
    if not b-1 in Way[a-1]:
        a2 += 1
    elif len(Way[a-1]) > 1:
        #a2 += 1
        a1 += 1

print(a2, a1+a2)