import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [{} for _ in range(N)]
for _ in range(M):
    a, b, l = map(int, input().split())
    if not l in graph[a-1].keys():
        graph[a-1][l] = 1
    else:
        graph[a-1][l] += 1
    if not l in graph[b-1].keys():
        graph[b-1][l] = 1
    else:
        graph[b-1][l] += 1

ans = 0
for n in range(N):
    for k, v in graph[n].items():
        if k == 2540//2:
            ans += v*(v-1)
        elif (2540-k) in graph[n].keys():
            ans += v*graph[n][2540-k]

ans //= 2
print(ans)