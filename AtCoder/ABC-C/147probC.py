N = int(input())
data = []
for _ in range(N):
    M = int(input())
    XY = [list(map(int, input().split())) for _ in range(M)]
    data.append((M, XY))

ans = 0
for bit in range(2**N):
    ok = True
    P = [-1]*N
    c = 0
    for i in range(N):
        M, XY = data[i]
        if bit & (1<<i):
            c += 1
            if P[i] == 0:
                ok = False
                break
            P[i] = 1
            for x, y in XY:
                if P[x-1] == -1:
                    P[x-1] = y
                elif P[x-1] != y:
                    ok = False
                    break
        else:
            if P[i] == 1:
                ok = False
            P[i] = 0
    if ok:
        ans = max(ans, c)
print(ans)