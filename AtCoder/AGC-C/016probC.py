H, W, sh, sw = map(int, input().split())

if H%sh == 0 and W%sw == 0:
    print("No")
else:
    print("Yes")
    state = [[1]*W for _ in range(H)]
    INF = 10**9
    for h in range(H):
        for w in range(W):
            if w%sw == sw-1 and h%sh == sh-1:
                state[h][w] = -INF
            elif w%sw == 0 and h%sh == 0:
                state[h][w] = INF - (sh*sw-1)
    for h in range(H):
        print(" ".join([str(a) for a in state[h]]))
