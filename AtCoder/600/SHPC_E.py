import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a-1].append((b-1, d))
    graph[b-1].append((a-1, d))


defined_n = 0
ok = True
even = True
Color = [-1]*N
D = [0]*N
c = 0
q = [0]
Color[0] = 0
while q:
    qq = []
    c ^= 1
    for p in q:
        for np, d in graph[p]:
            if Color[np] == -1:
                Color[np] = c
                D[np] = d - D[p]
                qq.append(np)
            elif Color[np] != c:
                if (d-D[p]-D[np]) % 2 != 0:
                    ok = False
                    break
                if c == 1:
                    defined_n = (d-D[p]-D[np])//2
                else:
                    defined_n = (D[np]+D[p]-d)//2
                even = False
                break
            elif D[np] != d-D[p]:
                ok = False
                break
        if not ok or not even: break
    if not ok or not even: break
    q = qq

if not ok:
    print(0)
elif not even:
    if defined_n <= 0:
        ok = False
    q = [0]
    score = [-1]*N
    score[0] = defined_n
    while q:
        qq = []
        for p in q:
            s = score[p]
            for np, d in graph[p]:
                if score[np] == -1:
                    if d-s <= 0:
                        ok = False
                        break
                    score[np] = d-s
                    qq.append(np)
                elif score[np] != d-s:
                    ok = False
                    break
            if not ok: break
        if not ok: break
        q = qq
    if not ok:
        print(0)
    else:
        print(1)
else:
    min_n = 0
    max_n = 10**14
    for n in range(N):
        if Color[n] == 0:
            min_n = max(-D[n], min_n)
        else:
            max_n = min(max_n, D[n])
    print(max(0, max_n-min_n-1))