N = int(input())
xyh = [list(map(int, input().split())) for _ in range(N)]

for x in range(101):
    for y in range(101):
        check = []
        for d in xyh:
            ifd0 = False
            if d[2] == 0:
                ifd0 = True
            ch = abs(d[0] - x) + abs(d[1] - y) + d[2]
            check.append([ch, ifd0])
        ifans = True
        for c in check:
            if c[0] - check[0][0] != 0:
                if ifd0:
                    continue
                ifans = False
                break
        if ifans:
            ans = [x, y, ch]
            break

print(' '.join([str(a) for a in ans]))