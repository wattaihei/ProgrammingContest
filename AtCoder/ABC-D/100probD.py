N, M = map(int, input().split())
XYZ = [list(map(int, input().split())) for _ in range(N)]

P = [[0 for _ in range(N)] for _ in range(8)]
for i, (x, y, z) in enumerate(XYZ):
    P[0][i] = x + y + z
    P[1][i] = x + y - z
    P[2][i] = x - y + z
    P[3][i] = x - y - z
    P[4][i] = -x + y + z
    P[5][i] = -x + y - z
    P[6][i] = -x - y + z
    P[7][i] = -x - y - z
ans = 0
for k in range(8):
    a = sum(sorted(P[k], reverse=True)[:M])
    ans = max(ans, a)
print(ans)
