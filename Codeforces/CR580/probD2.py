import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
L = max(A).bit_length()

ans = -1
graph = [[] for _ in range(N)]
V = []
for l in range(L):
    P = []
    for i in range(N):
        if (1 << l) & A[i]:
            P.append(i)
    if len(P) > 2:
        ans = 3
        break
    elif len(P) == 2:
        p0, p1 = P
        graph[p0].append(p1)
        graph[p1].append(p0)
        V.append(P)


def bfs(s, g):
    a = -1
    q = [s]
    checked = [False]*N
    checked[s] = True
    d = 0
    while q:
        qq = []
        d += 1
        for p in q:
            for np in graph[p]:
                if np == g:
                    if d == 1: continue
                    else: return d
                if not checked[np]:
                    qq.append(np)
                    checked[np] = True
        q = qq
    return -1

if ans == 3:
    print(3)
else:
    ans = 10**9
    for s, g in V:
        cycle = bfs(s, g)
        if cycle == -1:
            continue
        ans = min(cycle+1, ans)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
