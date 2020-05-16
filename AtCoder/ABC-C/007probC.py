R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
Map = [[0 if a == '.' else 1 for a in list(input())] for _ in range(R)]

qs = [(sx-1, sy-1)]

d = 0
ans = 0

while qs:
    #print(qs)
    qqs = []
    d += 1
    for q in qs:
        x, y = q
        nexts = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for nx, ny in nexts:
            if 0 <= nx <= R-1 and 0 <= ny <= C-1:
                if Map[nx][ny] == 0:
                    qqs.append((nx, ny))
                    Map[nx][ny] = 1
                if nx == gx-1 and ny == gy-1:
                    ans = d
    if ans > 0:
        break
    qs = qqs

print(ans)