import sys
input = sys.stdin.buffer.readline

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
state = [list(input().rstrip()) for _ in range(H)]

q = [(x1-1, y1-1)]
checked = [[-1]*W for _ in range(H)]
checked[x1-1][y1-1] = 0
while q:
    qq = []
    for x, y in q:
        d = checked[x][y]
        dx = 1
        while x+dx < H and state[x+dx][y] == ord(".") and dx <= K:
            if checked[x+dx][y] == -1:
                checked[x+dx][y] = d + 1
                qq.append((x+dx, y))
            elif checked[x+dx][y] >= d + 1:
                checked[x+dx][y] = d + 1
            else:
                break
            dx += 1
        dx = -1
        while x+dx >= 0 and state[x+dx][y] == ord(".") and dx >= -K:
            if checked[x+dx][y] == -1:
                checked[x+dx][y] = d + 1
                qq.append((x+dx, y))
            elif checked[x+dx][y] >= d+1:
                checked[x+dx][y] = d + 1
            else:
                break
            dx -= 1
        dy = 1
        while y+dy < W and state[x][y+dy] == ord(".") and dy <= K:
            if checked[x][y+dy] == -1:
                checked[x][y+dy] = d + 1
                qq.append((x, y+dy))
            elif checked[x][y+dy] >= d+1:
                checked[x][y+dy] = d+1
            else:
                break
            dy += 1
        dy = -1
        while y+dy >= 0 and state[x][y+dy] == ord(".") and dy >= -K:
            if checked[x][y+dy] == -1:
                checked[x][y+dy] = d + 1
                qq.append((x, y+dy))
            elif checked[x][y+dy] >= d+1:
                checked[x][y+dy] = d+1
            else:
                break
            dy -= 1
    q = qq

print(checked[x2-1][y2-1])