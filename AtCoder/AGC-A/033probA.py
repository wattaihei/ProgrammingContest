H, W = map(int, input().split()) # 横に2個

blacks = []
for i in range(H):
    for j, l in enumerate(list(input())):
        if l == '#':
            blacks.append([i, j])

c = -1
news = blacks[:]
while len(blacks) < H*W:
    if c >= 0:
        for new in news:
            blacks.append(new)
    next = []
    for new in news:
        i = new[0]
        j = new[1]
        nears = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
        for near in nears:
            ni = near[0]
            nj = near[1]
            if 0 <= ni and ni <= H-1 and 0 <= nj and nj <= W-1 and (not near in blacks) and (not near in next):
                next.append(near)

    news = next
    c += 1

print(c)
