import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


H, W = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(H)]
mod = 10**9 + 7

q = []
next = [[[] for _ in range(W)] for _ in range(H)]
pre = [[[] for _ in range(W)] for _ in range(H)]
for w in range(W):
    for h in range(H):
        nexts = []
        if h != 0: nexts.append((h-1, w))
        if h != H-1: nexts.append((h+1, w))
        if w != 0: nexts.append((h, w-1))
        if w != W-1: nexts.append((h, w+1))
        peak = True
        for nh, nw in nexts:
            if state[h][w] > state[nh][nw]:
                next[h][w].append((nh, nw))
            if state[h][w] < state[nh][nw]:
                peak = False
                pre[h][w].append((nh, nw))
        if peak:
            q.append((h, w))

score = [[1 for _ in range(W)] for _ in range(H)]
checked = [[False for _ in range(W)] for _ in range(H)]
for h, w in q:
    checked[h][w] = True

def dfs(h, w):
    checked[h][w] = True
    for nh, nw in next[h][w]:
        if not checked[nh][nw]:
            dfs(nh, nw)
        score[nh][nw] = (score[nh][nw] + score[h][w]) % mod


ans = 0
for h in range(H):
    for w in range(W):
        ans = (ans + score[h][w]) % mod

print(ans)