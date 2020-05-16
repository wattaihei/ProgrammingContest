N, D, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(D)]
ST = [list(map(int, input().split())) for _ in range(K)]

for s, t in ST:
    if s < t:
        p = True
    else:
        p = False
    #print('waaa', s, t)
    c = 0
    for l, r in LR:
        #print(l, r)
        c += 1
        if p and s >= l:
            if t <= r:
                break
            if s < r:
                s = r
        if (not p) and s <= r:
            if l <= t:
                break
            if s > l:
                s = l
    print(c)