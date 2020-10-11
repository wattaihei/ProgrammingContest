import sys
input = sys.stdin.readline


N = int(input())
XYP = [list(map(int, input().split())) for _ in range(N)]

INF = 10**18

def scores(Xs):
    L = len(Xs)
    dp = [[INF]*(L+1) for _ in range(L+1)]
    # k = 0
    init = 0
    for x, p in Xs:
        init += abs(x)*p
    if L == 0:
        return [0]
    # k = 1
    for ix, (x, p) in enumerate(Xs):
        dp[ix][0] = init
        score = 0
        for jx, (y, q) in enumerate(Xs):
            score += min(abs(y)*q, abs(x-y)*q)
        dp[ix][1] = score
    
    # k > 1
    for k in range(1, L):
        for ix, (x, p) in enumerate(Xs):
            for iy in range(ix+1, L):
                y, q = Xs[iy]
                tmp = dp[ix][k]
                for iz in range(ix+1, L):
                    z, r = Xs[iz]
                    new = abs(z-y)
                    pre = min(abs(z), abs(z-x))
                    if new < pre:
                        tmp += (new - pre)*r
                dp[iy][k+1] = min(dp[iy][k+1], tmp)
    
    ret = [INF]*(L+1)
    for k in range(L+1):
        for j in range(L+1):
            ret[k] = min(dp[j][k], ret[k])

    return ret

ans = [INF]*(N+1)
for bit in range(1<<N):
    Xs = []
    Ys = []
    for i, (x, y, p) in enumerate(XYP):
        if (1<<i)&bit:
            Xs.append((x, p))
        else:
            Ys.append((y, p))

    Xs.sort()
    Ys.sort()
    dpx = scores(Xs)
    dpy = scores(Ys)
    for i, x in enumerate(dpx):
        for j, y in enumerate(dpy):
            ans[i+j] = min(ans[i+j], x+y)

print(*ans, sep="\n")
