import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

c = 0
for n in range(N):
    ok = True
    for np in graph[n]:
        if H[np] >= H[n]:
            ok = False
            break
    if ok:
        c += 1
print(c)