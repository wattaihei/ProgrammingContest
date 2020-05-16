import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

q = [0]
color = [-1]*N
color[0] = 0
while q:
    qq = []
    for p in q:
        for np in graph[p]:
            if color[np] == -1:
                color[np] = color[p] ^ 1
                qq.append(np)
    q = qq


Cs = set()
Vs = set()
ans2 = N-1
for n in range(N):
    if len(graph[n]) == 1:
        Cs.add(color[n])
        Vs.add(graph[n][0])
        ans2 -= 1

ans1 = 1 if len(Cs) == 1 else 3
ans2 += len(Vs)
print(ans1, ans2)