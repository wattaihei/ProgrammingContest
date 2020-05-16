H, W = map(int, input().split())
state = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if state[h][w] == 's':
            s = (h, w)
        if state[h][w] == 'g':
            g = (h, w)

checked = [[False for _ in range(W)] for _ in range(H)]
q = [s]
checked[s[0]][s[1]] = True
def bfs(q):
    black = []
    while q:
        qq = []
        for ph, pw in q:
            nexts = []
            if ph != 0: nexts.append((ph-1, pw))
            if ph != H-1: nexts.append((ph+1, pw))
            if pw != 0: nexts.append((ph, pw-1))
            if pw != W-1: nexts.append((ph, pw+1))
            for nh, nw in nexts:
                if not checked[nh][nw]:
                    if state[nh][nw] == '.':
                        qq.append((nh, nw))
                        checked[nh][nw] = True
                    elif state[nh][nw] == 'g':
                        return True, []
                    elif state[nh][nw] == '#':
                        black.append((nh, nw))
                        checked[nh][nw] = True
        q = qq
    return False, black

for _ in range(3):
    ok, q = bfs(q)
    if ok: break
if ok:
    print('YES')
else:
    print('NO')