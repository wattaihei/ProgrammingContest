import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))


Parent = [None for _ in range(2*N+1)]
Points = [(2*N, 0), (0, A[0])]
Parent[0] = (2*N, A[0])
Parent[2*N] = (-1, 1)

for i, a in enumerate(A):
    if i == 0: continue
    lastp, lastd = Points.pop()
    while True:
        if a <= Points[-1][1]:
            lastp, lastd = Points.pop()
        else:
            break
    tmprootdepth = min(lastd, a) - 1
    if tmprootdepth == Points[-1][1]:
        Parent[i] = (Points[-1][0], a-tmprootdepth)
        Points.append((i, a))
    else:
        Parent[lastp] = (i+N, lastd-tmprootdepth)
        Parent[i] = (i+N, a-tmprootdepth)
        Parent[i+N] = (Points[-1][0], tmprootdepth-Points[-1][1])
        Points.append((i+N, tmprootdepth))
        Points.append((i, a))

graph = [[] for _ in range(2*N+1)]
for n in range(2*N):
    if not Parent[n] is None:
        graph[Parent[n][0]].append((Parent[n][1], n))

def dfs(p, span, checked):
    checked[p] = True
    W = 0
    update = False
    for nd, np in graph[p]:
        if not checked[np]:
            W += dfs(np, span, checked)
            update = True
    dis_to_parent = Parent[p][1]
    if not update:
        dis_to_parent -= 1
        W = 1
    for _ in range(dis_to_parent):
        W = (W-1)//span
        if W <= 0:
            W = 0
            break
        W += 1
    return W

pre = -1
canonly = True
for a in A:
    if a <= pre:
        canonly = False
        break
    pre = a

if canonly:
    print(1)
else:
    l = 1
    r = N+1
    while r-l > 1:
        m = (l+r)//2
        W = dfs(2*N, m, [False]*(2*N+1))
        if W > 0:
            l = m
        else:
            r = m

    print(r)