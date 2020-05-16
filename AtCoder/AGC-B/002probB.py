N, M = map(int, input().split()) # 横に2個
XY = [list(map(int, input().split())) for _ in range(M)]

balls = [1 for _ in range(N)]
red = [False for _ in range(N)]
red[0] = True
for i in range(M):
    x, y = XY[i]
    x -= 1
    y -= 1
    if red[x]:
        red[y] = True
        if balls[x] == 1:
            red[x] = False
    balls[x] -= 1
    balls[y] += 1
print(sum(red))
