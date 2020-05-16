import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
A = [[] for _ in range(H+1)]
for _ in range(N):
    X, Y = map(int, input().split())
    A[X].append(Y)

ans = H
Ymax = 1
for n in range(1, H):
    cango = True
    for y in A[n+1]:
        if y <= Ymax:
            ans = n
            break
        elif y == Ymax+1:
            cango = False
    if ans != H:
        break
    if cango:
        Ymax += 1
print(ans)