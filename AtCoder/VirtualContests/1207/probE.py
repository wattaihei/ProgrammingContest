import sys
input = sys.stdin.readline

S = input().rstrip()
gx, gy = map(int, input().split())
L = len(S)

XY = [[], []]
d = 0
c = 0
begin = True
for s in S:
    if begin and s == "F":
        gx -= 1
    elif s == 'T':
        begin = False
        if c > 0:
            XY[d].append(c)
        d ^= 1
        c = 0
    else:
        c += 1
if c > 0:
    XY[d].append(c)

XY[0].append(abs(gx))
XY[1].append(abs(gy))

ans = True
for X in XY:
    G = sum(X)
    if G%2 != 0:
        ans = False
        break
    G //= 2
    ok = False
    W = len(X)
    dp = [False]*(G+1)
    dp[0] = True
    for i, x in enumerate(X):
        for g in reversed(range(G+1)):
            if g >= x:
                dp[g] = dp[g-x] or dp[g]
        if dp[G]:
            ok = True
            break
    ans = ok and ans
print("Yes" if ans else "No")