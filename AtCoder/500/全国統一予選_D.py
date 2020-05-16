import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
num_of_parent = [0]*N
for _ in range(N+M-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    num_of_parent[b-1] += 1

for i in range(N):
    if num_of_parent[i] == 0:
        root = i
        break

Parent = [None]*N
Parent[root] = 0
q = [root]
while q:
    qq = []
    for p in q:
        for np in graph[p]:
            num_of_parent[np] -= 1
            if num_of_parent[np] == 0:
                Parent[np] = p+1
                qq.append(np)
    q = qq

for p in Parent:
    print(p)