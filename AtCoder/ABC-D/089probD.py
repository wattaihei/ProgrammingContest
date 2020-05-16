H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

place = [None]*(H*W+1)
for h in range(H):
    for w in range(W):
        place[A[h][w]] = (h, w)
place[0] = (0, 0)
dis = [[0 for _ in range((H*W)//D+1)] for _ in range(D)]
for i, (x, y) in enumerate(place):
    if i <= D:
        continue
    bx, by = place[i-D]
    dis[i%D][i//D] = dis[i%D][i//D-1] + abs(x-bx) + abs(y-by)


for l, r in LR:
    ans = dis[r%D][r//D] - dis[l%D][l//D]
    print(ans)