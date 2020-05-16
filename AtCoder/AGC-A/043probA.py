import sys
input = sys.stdin.readline

H, W = map(int, input().split())
state = [list(input().rstrip()) for _ in range(H)]

def next(h, w):
    ret = []
    if h != H-1:
        ret.append((h+1, w))
    if w != W-1:
        ret.append((h, w+1))

dp = [[0]*(W) for _ in range(H)]

for w in range(W-1):
    t = dp[0][w]
    if state[0][w] != state[0][w+1]:
        t += 1
    dp[0][w+1] = t

for h in range(1, H):
    tmp = dp[h-1][0]
    if state[h-1][0] != state[h][0]:
        tmp += 1
    dp[h][0] = tmp
    for w in range(1, W):
        t1 = dp[h][w-1]
        t2 = dp[h-1][w]
        if state[h][w-1] != state[h][w]:
            t1 += 1
        if state[h-1][w] != state[h][w]:
            t2 += 1
        dp[h][w] = min(t1, t2)

p = dp[H-1][W-1]
if p%2 == 0:
    if state[0][0] == ".":
        ans = p//2
    else:
        ans = p//2+1
else:
    ans = (p+1)//2
print(ans)