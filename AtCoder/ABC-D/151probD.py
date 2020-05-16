import sys
input = sys.stdin.readline

H, W = map(int, input().split())
state = [list(input().rstrip()) for _ in range(H)]

def nexts(h, w):
    pq = []
    if h != 0: pq.append((h-1, w))
    if w != 0: pq.append((h, w-1))
    if h != H-1: pq.append((h+1, w))
    if w != W-1: pq.append((h, w+1))
    return pq


def bfs(sh, sw):
    Ds = [[-1]*W for _ in range(H)]
    q = [(sh, sw)]
    d = 0
    Ds[sh][sw] = 0
    while q:
        qq = []
        d += 1
        for h, w in q:
            for nh, nw in nexts(h, w):
                if state[nh][nw] == "#":
                    Ds[nh][nw] = -2
                elif Ds[nh][nw] == -1:
                    Ds[nh][nw] = d
                    qq.append((nh, nw))
        q = qq
    
    maxd = 0
    for h in range(H):
        for w in range(W):
            if maxd < Ds[h][w]:
                maxd = Ds[h][w]
                lh, lw = h, w
    return maxd

ans = 0
for h in range(H):
    for w in range(W):
        if state[h][w] == ".":
            d = bfs(h, w)
            ans = max(ans, d)

print(ans)