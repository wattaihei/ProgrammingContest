import sys
input = sys.stdin.buffer.readline
import heapq as hp



N, M = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]

Vs = [set() for _ in range(N)]
for i, (x, y) in enumerate(XY):
    Vs[x-1].add(i)
    Vs[y-1].add(i)

q = []
for vnum, a in enumerate(A):
    hp.heappush(q, (len(Vs[vnum])-a, vnum))

checked = [False]*N
ans = [-1]*M
while q:
    fl, vnum = hp.heappop(q)
    if checked[vnum]: continue
    if fl > 0:
        ans = []
        break
    updateV = {}
    for edge in Vs[vnum]:
        ans[edge] = vnum+1
        x, y = XY[edge]
        x -= 1; y -= 1
        if x in updateV:
            updateV[x].add(edge)
        else:
            updateV[x] = {edge}
        if y in updateV:
            updateV[y].add(edge)
        else:
            updateV[y] = {edge}
    checked[vnum] = True
    for v, edges in updateV.items():
        for edge in edges:
            Vs[v].remove(edge)
        #hp.heappush(q, (len(Vs[v])-A[v], v))

if not ans:
    print("DEAD")
else:
    print("ALIVE")
    print(" ".join([str(a) for a in ans]))