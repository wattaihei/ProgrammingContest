import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
Ed = {}
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    Ed[(a-1)*N+b-1] = i
    Ed[(b-1)*N+a-1] = i

q = [0]
checked = [False]*N
checked[0] = True

V_color = [None]*N
V_color[0] = 0

ans = [None]*(N-1)
while q:
    qq = []
    for p in q:
        c = V_color[p]
        t = 1
        for np in graph[p]:
            if not checked[np]:
                checked[np] = True
                qq.append(np)
                ind = Ed[p*N+np]
                if t == c:
                    t += 1
                ans[ind] = t
                V_color[np] = t
                t += 1
    q = qq

print(max(ans))
for a in ans:
    print(a)