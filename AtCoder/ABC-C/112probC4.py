N = int(input())
XYH = [list(map(int, input().split())) for _ in range(N)]

for x0 in range(101):
    for y0 in range(101):
        a = -1
        ok = True
        for x, y, h in XYH:
            if h == 0:
                continue
            if a == -1:
                a = abs(x-x0) + abs(y-y0) + h
                continue
            if a != abs(x-x0) + abs(y-y0) + h:
                ok = False
                break
        for x, y, h in XYH:
            if h != max(a- abs(x0-x) - abs(y0-y), 0):
                ok = False
        if ok:
            print(x0, y0, a)
            break
    if ok:
        break