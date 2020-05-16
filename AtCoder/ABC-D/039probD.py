import sys
input = sys.stdin.readline

H, W = map(int, input().split())
state = [input().rstrip() for _ in range(H)]

ans = [list("."*W) for _ in range(H)]

def nexts(h, w):
    next = [(h, w)]
    if h != 0:
        next.append((h-1, w))
        if w != 0:
            next.append((h-1, w-1))
        if w != W-1:
            next.append((h-1, w+1))
    if h != H-1:
        next.append((h+1, w))
        if w != 0:
            next.append((h+1, w-1))
        if w != W-1:
            next.append((h+1, w+1))
    if w != 0:
        next.append((h, w-1))
    if w != W-1:
        next.append((h, w+1))
    return next

for h in range(H):
    for w in range(W):
        Nexts = nexts(h, w)
        all_black = True
        for nh, nw in Nexts:
            if state[nh][nw] == ".":
                all_black = False
        if all_black:
            ans[h][w] = "#"

ok = True
for h in range(H):
    for w in range(W):
        if state[h][w] == "#":
            near = False
            Nexts = nexts(h, w)
            for nh, nw in Nexts:
                if ans[nh][nw] == "#":
                    near = True
                    break
            if not near:
                ok = False
                break

if not ok:
    print("impossible")
else:
    print("possible")
    for a in ans:
        print("".join(a))