import sys
input = sys.stdin.readline

H, W = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(H)]
mod = 10**9+7

q = []
score = [[1]*W for _ in range(H)]
before = [[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        nexts = []
        if h != 0: nexts.append((h-1, w))
        if h != H-1: nexts.append((h+1, w))
        if w != 0: nexts.append((h, w-1))
        if w != W-1: nexts.append((h, w+1))
        minimum = True
        for nh, nw in nexts:
            if state[h][w] > state[nh][nw]:
                before[h][w] += 1
                minimum = False
        if minimum:
            q.append((h, w))

while q:
    qq = []
    for h, w in q:
        nexts = []
        if h != 0: nexts.append((h-1, w))
        if h != H-1: nexts.append((h+1, w))
        if w != 0: nexts.append((h, w-1))
        if w != W-1: nexts.append((h, w+1))
        for nh, nw in nexts:
            if state[h][w] >= state[nh][nw]: continue
            score[nh][nw] += score[h][w]
            score[nh][nw] %= mod
            before[nh][nw] -= 1
            if before[nh][nw] == 0:
                qq.append((nh, nw))
    q = qq

ans = 0
for h in range(H):
    for w in range(W):
        ans = (ans + score[h][w]) % mod

print(ans)