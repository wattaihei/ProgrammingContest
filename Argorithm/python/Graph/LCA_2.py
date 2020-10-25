from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
prv = [None]*N
G = [None]*N
for v in range(N):
    k, *G[v] = map(int, readline().split())
    for c in G[v]:
        prv[c] = v

depth = [0]*N
que = deque([0])
while que:
    v = que.popleft()
    d = depth[v]
    for w in G[v]:
        depth[w] = d + 1
        que.append(w)

LV = (N-1).bit_length()
def construct(prv):
    kprv = [prv]
    S = prv
    for k in range(LV):
        T = [0]*N
        for i in range(N):
            if S[i] is None:
                continue
            T[i] = S[S[i]]
        kprv.append(T)
        S = T
    return kprv

def lca(u, v, kprv, depth):
    dd = depth[v] - depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd

    # assert depth[u] <= depth[v]
    for k in range(LV+1):
        if dd & 1:
            v = kprv[k][v]
        dd >>= 1

    # assert depth[u] == depth[v]
    if u == v:
        return u

    for k in range(LV-1, -1, -1):
        pu = kprv[k][u]; pv = kprv[k][v]
        if pu != pv:
            u = pu; v = pv

    # assert kprv[0][u] == kprv[0][v]
    return kprv[0][u]


kprv = construct(prv)

Q = int(readline())
ans = []
for q in range(Q):
    u, v = map(int, readline().split())
    ans.append(lca(u, v, kprv, depth))
write("\n".join(map(str, ans)))
write("\n")