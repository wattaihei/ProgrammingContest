import sys
input = sys.stdin.buffer.readline

N = int(input())
Edges = []
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    Edges.append((a-1, b-1))

stack = [0]
pre = [-1]*N
while stack:
    p = stack.pop()
    if p>= 0:
        for np in graph[p]:
            if np != 0 and pre[np] == -1:
                pre[np] = p
                stack.append(np)

Score = [0]*N
Q = int(input())
for _ in range(Q):
    t, e, x = map(int, input().rstrip().split())
    a, b = Edges[e-1]
    if t == 1:
        if pre[b] == a:
            Score[0] += x
            Score[b] -= x
        else:
            Score[a] += x
    else:
        if pre[b] == a:
            Score[b] += x
        else:
            Score[0] += x
            Score[a] -= x

q = [0]
checked = [False]*N
checked[0] = True
while q:
    qq = []
    for p in q:
        for np in graph[p]:
            if not checked[np] and np != pre[p]:
                checked[np] = True
                Score[np] += Score[p]
                qq.append(np)
    q = qq

print(*Score, sep="\n")