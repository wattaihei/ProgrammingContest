import sys
input = sys.stdin.buffer.readline

mod = 10**9+7

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

cols = set()
lmin = -10**18
invs = {}
remain = []
for l,r in LR:
    cols.add(l)
    cols.add(r)
    lmin = max(lmin, l)
    invs[r-l] = pow(r-l, mod-2, mod)
    remain.append(r-l)




ind_to_col = sorted(list(cols))
col_to_ind = {k:i for i, k in enumerate(ind_to_col)}
L = len(ind_to_col)

Ps = [[] for _ in range(L)]
for ind, (l, r) in enumerate(LR):
    il, ir = col_to_ind[l], col_to_ind[r]
    for i in range(il, ir):
        Ps[i].append((ind, r-l))

ans = 0
for iq in reversed(range(col_to_ind[lmin], L-1)):
    l, r = ind_to_col[iq], ind_to_col[iq+1]
    points = len(Ps[iq])
    # s = (l + r*(points)) * pow(points+1, mod-2, mod) % mod
    d = r-l
    dp = [0 for _ in range(points)]
    for pind, p in Ps[iq]:
        pa = invs[p] * d % mod
        pb = invs[p] * (remain[pind] - d) % mod
        dp[pa]
        remain[pind] -= d
    ans = (ans + s) % mod

for n in range(1, N+2):
    ans = (ans * n) % mod
for l, r in LR:
    ans = (ans * (r-l)) % mod

print(ans)