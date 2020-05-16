import sys
input = sys.stdin.readline

N, K = map(int, input().split())
white = [[0]*(K+1) for _ in range(2*K+1)]
black = [[0]*(K+1) for _ in range(2*K+1)]
for _ in range(N):
    str_h, str_w, c = map(str, input().rstrip().split())
    h = int(str_h)%(2*K)
    w = int(str_w)%(2*K)
    if c == "W":
        if w >= K:
            if h >= K:
                white[h-K+1][w-K+1] += 1
            else:
                white[h+K+1][w-K+1] += 1
        else:
            white[h+1][w+1] += 1
    else:
        if w >= K:
            if h >= K:
                black[h-K+1][w-K+1] += 1
            else:
                black[h+K+1][w-K+1] += 1
        else:
            black[h+1][w+1] += 1

for h in range(1, 2*K+1):
    for w in range(1, K+1):
        white[h][w] += white[h][w-1] + white[h-1][w] - white[h-1][w-1]
        black[h][w] += black[h][w-1] + black[h-1][w] - black[h-1][w-1]

ans = 0
for h in range(K+1):
    for w in range(K+1):
        b1 = black[h][w]
        b2 = black[h+K][K] - black[h+K][w] - black[h][K] + black[h][w]
        b3 = black[2*K][w] - black[h+K][w]
        w1 = white[h][K] - white[h][w]
        w2 = white[h+K][w] - white[h][w]
        w3 = white[2*K][K] - white[2*K][w] - white[h+K][K] + white[h+K][w]
        ans = max(ans, b1+b2+b3+w1+w2+w3)

        b1 = white[h][w]
        b2 = white[h+K][K] - white[h+K][w] - white[h][K] + white[h][w]
        b3 = white[2*K][w] - white[h+K][w]
        w1 = black[h][K] - black[h][w]
        w2 = black[h+K][w] - black[h][w]
        w3 = black[2*K][K] - black[2*K][w] - black[h+K][K] + black[h+K][w]
        ans = max(ans, b1+b2+b3+w1+w2+w3)

print(ans)