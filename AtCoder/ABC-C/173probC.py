import sys
input = sys.stdin.readline

H, W, K = map(int, input().split())
state = [input().rstrip() for _ in range(H)]

ans = 0
for bit1 in range(1<<H):
    for bit2 in range(1<<W):
        c = 0
        for h in range(H):
            for w in range(W):
                if state[h][w] == "#" and not bit1&(1<<h) and not bit2&(1<<w):
                    c += 1
        if c == K:
            ans += 1
print(ans)