import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ok = True
color = [-1]*N
q = [0]
color[0] = 0
c = 0
while q:
    qq = []
    c ^= 1
    for p in q:
        for np in graph[p]:
            if color[np] == -1:
                color[np] = c
                qq.append(np)
            elif color[np] != c:
                ok = False
                break
    if not ok: break
    q = qq

if not ok:
    ans = N*(N-1)//2 - M
else:
    s = sum(color)
    ans = s*(N-s) - M
print(ans)