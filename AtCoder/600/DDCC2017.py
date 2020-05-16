import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A, B = map(int, input().split())
state = [list(input().rstrip()) for _ in range(H)]

def isS(h, w):
    return state[h][w] == "S"

four = 0
of = False
ee = False
t1 = 0
t2 = 0
for h in range(H//2):
    for w in range(W//2):
        if isS(h, w) and isS(H-1-h, w) and isS(h, W-1-w) and isS(H-1-h, W-1-w):
            four += 1
        elif not isS(h, w) and not isS(H-1-h, w) and not isS(h, W-1-w) and not isS(H-1-h, W-1-w):
            continue
        else:
            of = True
            up = False
            if isS(h, w) and isS(H-1-h, w):
                t1 += 1
                up = True
            if isS(h, W-1-w) and isS(H-1-h, W-1-w):
                t1 += 1
                up = True
            if isS(h, w) and isS(h, W-1-w):
                t2 += 1
                up = True
            if isS(H-1-h, w) and isS(H-1-h, W-1-w):
                t2 += 1
                up = True
            if not up:
                ee = True

ans = four*(max(A, B) + A+B)
a1 = t1*A
a2 = t2*B
if of:
    ans += A+B
if not (ee or t2 > 0) and t1 > 0:
    a1 -= A
if not (ee or t1 > 0) and t2 > 0:
    a2 -= B
ans += max(a1, a2)
print(ans)
