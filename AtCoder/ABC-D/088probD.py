H, W = map(int, input().split())
state = [[0 if s == '.' else 1 for s in list(input())] for _ in range(H)]

checked = [[False for _ in range(W)] for _ in range(H)]
qs = [(0, 0)]
checked[0][0] = True
goal = False
d = 0
while qs:
    qqs = []
    for qx, qy in qs:
        nexts = [(qx, qy+1), (qx, qy-1), (qx+1, qy), (qx-1, qy)]
        for nx, ny in nexts:
            if 0 <= nx <= W-1 and 0 <= ny <= H-1:
                if checked[ny][nx] or state[ny][nx] == 1:
                    continue
                qqs.append((nx, ny))
                checked[ny][nx] = True
            if nx == W-1 and ny == H-1:
                goal = True
                break
    d += 1
    if goal:
        break
    qs = qqs

black = 0
for h in range(H):
    for w in range(W):
        if state[h][w] == 1:
            black += 1

if goal:
    ans = H*W - black - d - 1
else:
    ans = -1

print(ans)