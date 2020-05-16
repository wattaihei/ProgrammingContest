import sys
input = sys.stdin.readline
INF = 10**14

R, G, B = map(int, input().split())

# [l, r) の制限でC個を中心pから分配
def score(C, p, l, r):
    if r <= p:
        d = p-r+1
        return (d + C+d-1)*C//2
    if l > p:
        d = l-p
        return (d + C+d-1)*C//2
    rmax = r-p-1
    lmax = p-l
    if lmax < rmax:
        rmax, lmax = lmax, rmax
    d1 = (C-1)//2
    d2 = C//2
    if (d1 <= rmax and d2 <= lmax):
        return (d1+1)*d1//2 + (d2+1)*d2//2
    if d1 > rmax:
        p1 = rmax
        p2 = C - rmax - 1
        return (p1+1)*p1//2 + (p2+1)*p2//2
    else:
        p1 = lmax
        p2 = C - lmax - 1
        return (p1+1)*p1//2 + (p2+1)*p2//2


ans = INF
for g in range(-1000, 1000):
    gs = score(G, 0, g, g+G)
    rs = score(R, -100, -INF, g)
    bs = score(B, 100, g+G, INF)
    ans = min(ans, gs+rs+bs)
print(ans)