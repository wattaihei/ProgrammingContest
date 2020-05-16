N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(start):
    checked = [False]*N
    q = [start]
    c = -1
    while q:
        qq = []
        c += 1
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
        if not qq:
            break
        q = qq
    return c, q

_, q = bfs(0)
d, _ = bfs(q[0])
if d%3 == 1:
    print('Second')
else:
    print("First")