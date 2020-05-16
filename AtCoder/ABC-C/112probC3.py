N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for cx in range(101):
    for cy in range(101):
        H = -1
        ok = True
        for x, y, h in P:
            if h == 0:
                continue
            Hi = abs(x-cx) + abs(y-cy) + h
            if H == -1:
                H = Hi
                continue
            if Hi != H:
                ok = False
                break
        if not ok:
            continue
        for x, y, h in P:
            if h != max(H-abs(cx-x)-abs(cy-y), 0):
                ok = False
        if ok:
            print(cx, cy, H)
            break
    if ok:
        break