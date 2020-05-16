H, W = map(int, input().split()) # 横に2個

c = 0
for _ in range(H):
    for a in input():
        if a == '#':
            c += 1

if c == H + W - 1:
    print('Possible')
else:
    print('Impossible')