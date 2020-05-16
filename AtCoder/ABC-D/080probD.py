from operator import itemgetter

N, C = map(int, input().split())
STC = [list(map(int, input().split())) for _ in range(N)]

P = [[] for _ in range(C)]
for s, t, c in STC:
    P[c-1].append((s, t))

Q = []
for ps in P:
    ps.sort(key=itemgetter(0))
    if not ps:
        continue
    for i, (s, t) in enumerate(ps):
        if i == 0:
            pres = s
            pret = t
            continue
        if s == pret:
            pret = t
            continue
        Q.append((pres-1, pret))
        pres = s
        pret = t
    Q.append((pres-1, pret))

imos = [0 for _ in range(100003)]
for qx, qy in Q:
    imos[qx] += 1
    imos[qy] -= 1

for i in range(100002):
    imos[i] += imos[i-1]
print(max(imos))