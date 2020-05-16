import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(s):
    checked = [False]*N
    q = [s]
    checked[s] = True
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    qq.append(np)
        if not qq:
            break
        q = qq
    return q[0]



def search(p, now, checked, end):
    now.append(p)
    if p == end:
        return now
    update = False
    for np in graph[p]:
        if not checked[np]:
            update = True
            checked[np] = True
            l = search(np, now, checked, end)
            if l:
                return l
    if not update:
        now.pop()
        return []


def dfs(p, checked, vpath, score):
    s = 1
    vp = vpath[p]
    for np in graph[p]:
        if np == vp:
            checked[np] = True
            continue
        if not checked[np]:
            checked[np] = True
            a, score = dfs(np, checked, vpath, score)
            s += a
    if vp != -1:
        a, score = dfs(vp, checked, vpath, score)
        s += a
    #print(p, s, score)
    return s, score+s

v1 = bfs(0)
v2 = bfs(v1)
path = search(v1, [], [False]*N, v2)
v12 = [-1]*N
v21 = [-1]*N
for i in range(len(path)-1):
    v12[path[i]] = path[i+1]
    v21[path[i+1]] = path[i]
#print(v1, v12)
checked1 = [False]*N
checked1[v1] = True
_, s1 = dfs(v1, checked1, v12, 0)

checked2 = [False]*N
checked2[v2] = True
_, s2 = dfs(v2, checked2, v21, 0)

print(max(s1, s2))