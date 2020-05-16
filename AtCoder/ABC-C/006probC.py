N, M = map(int, input().split())

a = False
for x in range(N+1):
    y = -2*x + 4*N - M
    z = x - 3*N + M
    if y >= 0 and z >= 0:
        a = True
        print(x, y, z)
        break
if not a:
    print(-1, -1, -1)