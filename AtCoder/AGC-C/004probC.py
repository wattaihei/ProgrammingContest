import sys
input = sys.stdin.readline

H, W = map(int, input().split())
state = [list(input().rstrip()) for _ in range(H)]

ans = [[["."]*W for _ in range(H)] for _ in range(2)]

color = 0 # base color
was_blank = False # whether previous row was blank
for h in range(H):
    must_color = []
    for w in range(W):
        if state[h][w] == "#":
            must_color.append(w)
    if not must_color:
        if not was_blank:
            color ^= 1
        for w in range(1, W):
            ans[color][h][w] = "#"
        ans[color^1][h][0] = "#"
        was_blank = True
    else:
        color ^= 1
        for w in range(W):
            ans[color][h][w] = "#"
        for w in must_color:
            ans[color^1][h][w] = "#"
        was_blank = False

for h in range(H):
    print("".join(ans[0][h]))
print()
for h in range(H):
    print("".join(ans[1][h]))