from fractions import gcd

N, M, Q = map(int, input().split())
data = []
for _ in range(Q):
    A = list(map(int, input().split()))
    data.append(A)

C = gcd(N, M)
rn, rm = N//C, M//C

def zone(px, py):
    if px == 1:
        return (py-1)//rn
    else:
        return (py-1)//rm

for sx, sy, ex, ey in data:
    zs = zone(sx, sy)
    ze = zone(ex, ey)
    if zs == ze:
        print('YES')
    else:
        print('NO')