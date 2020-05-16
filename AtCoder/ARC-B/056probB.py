import sys
input = sys.stdin.readline

N, M, S = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

used = [False]*N
for n in reversed(range(N)):
    if n == S-1:
        used[n] = True
    else:
        for m in graph[n]:
            if used[m]:
                used[n] = True
                break

for i in range(N):
    if used[i]:
        print(i+1)
