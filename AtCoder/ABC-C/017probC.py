N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]


POINT = [0]*(M+2)
S = 0
for l, r, s in ABC:
    S += s
    POINT[l] += s
    POINT[r+1] -= s

point = []
p = 0
for m in range(M+2):
    p += POINT[m]
    point.append(p)

print(S-min(point[1:-1]))