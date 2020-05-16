import sys
sys.setrecursionlimit(600000)

N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def dfs(p, checked, now):
    #print(p, checked, now)
    if p == N-1:
        return now, True
    ok = False
    for q in graph[p]:
        if not checked[q]:
            now.append(q)
            checked[q] = True
            nbw, ok1 = dfs(q, checked, now)
            if ok1:
                bw = nbw
                ok = True
    if not ok:
        now.pop()
        return now, False
    return bw, True

checked = [False for _ in range(N)]
checked[0] = True
bw, ok = dfs(0, checked, [0])
#print(bw)

between = [0 for _ in range(N)]
k = len(bw)
if k % 2 == 0:
    s0 = bw[k//2-1]
    sN = bw[k//2]
else:
    s0 = bw[k//2]
    sN = bw[k//2+1]
between[s0] = True
between[sN] = True

def dfs2(p, checked, c):
    c += 1
    for q in graph[p]:
        if not checked[q]:
            checked[q] = True
            c = dfs2(q, checked, c)
    return c

c0 = dfs2(s0, between, 0)
cN = dfs2(sN, between, 0)
#print(c0, cN)



if cN < c0:
    print('Fennec')
else:
    print('Snuke')