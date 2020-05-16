H, W = map(int, input().split())
state = [list(input()) for _ in range(H)]

rmh = 0
for h in range(H):
    h -= rmh
    ok = True
    for w in range(W):
        if state[h][w] == '#':
            ok = False
            break
    if ok:
        state.pop(h)
        rmh += 1
H -= rmh
rmw = 0
for w in range(W):
    w -= rmw
    ok = True
    for h in range(H):
        if state[h][w] == '#':
            ok = False
            break
    if ok:
        for h in range(H):
            state[h].pop(w)
        rmw += 1

for s in state:
    print(''.join(s))