import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

NUM = [-1]*N
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    NUM[a-1] = b
    root = a-1

MIN = [None]*N
MAX = [None]*N

rootnum = NUM[root]
checked = [False]*N
def dfs(p, d):
    checked[p] = True
    minnum, maxnum = rootnum-d, rootnum+d
    ok = True
    for np in graph[p]:
        if not checked[np]:
            ok = dfs(np, d+1) and ok
            if MIN[np]%2 == minnum%2 or MAX[np]%2 == minnum%2:
                ok = False
            minnum = max(minnum, MIN[np]-1)
            maxnum = min(maxnum, MAX[np]+1)
    if maxnum < minnum:
        ok = False
    if NUM[p] != -1:
        if not (minnum <= NUM[p] <= maxnum):
            ok = False
        MAX[p] = NUM[p]
        MIN[p] = NUM[p]
    else:
        MAX[p] = maxnum
        MIN[p] = minnum
    return ok

if not dfs(root, 0):
    print("No")
else:
    print("Yes")
    checked = [False]*N
    q = [root]
    while q:
        qq = []
        for p in q:
            pnum = NUM[p]
            for np in graph[p]:
                if not checked[np]:
                    if NUM[np] == -1:
                        if MIN[np] <= pnum+1 <= MAX[np]:
                            NUM[np] = pnum+1
                        else:
                            NUM[np] = pnum-1
                    qq.append(np)
                    checked[np] = True
        q = qq
    
    print(*NUM, sep="\n")