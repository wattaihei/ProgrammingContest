import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ok = True
for i in range(N):
    if len(graph[i]) == 2:
        ok = False
if ok:
    print("YES")
else:
    print("NO")