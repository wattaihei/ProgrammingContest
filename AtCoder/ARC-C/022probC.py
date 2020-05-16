import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def bfs(p):
    checked = [False]*N
    checked[p] = True
    q = [p]
    while q:
        qq = []
        for p in q:
            last = p
            for np in graph[p]:
                if not checked[np]:
                    qq.append(np)
                    checked[np] = True
        q = qq
    return last

a1 = bfs(0)
a2 = bfs(a1)
print(a1+1, a2+1)