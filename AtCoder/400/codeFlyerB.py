N, Q = map(int, input().split())
X = list(map(int, input().split()))
C = []
D = []
Zs = set(X)
for _ in range(Q):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)
    Zs.add(c)

Z = sorted(list(Zs))

P = {}
for i, z in enumerate(Z):
    P[z] = i


