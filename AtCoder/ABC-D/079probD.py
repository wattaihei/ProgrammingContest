H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

for i in range(10):
    for j in range(10):
        for k in range(10):
            C[j][k] = min(C[j][k], C[j][i] + C[i][k])

ans = 0
for h in range(H):
    for w in range(W):
        a = A[h][w]
        if a == -1:
            continue
        ans += C[a][1]
print(ans)