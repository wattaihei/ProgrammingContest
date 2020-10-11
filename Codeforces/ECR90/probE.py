import sys
input = sys.stdin.readline

Q = int(input())
NK = [list(map(int, input().split())) for _ in range(Q)]

INF = 10**19


def make(x, a, need=True):
    ret = ""
    if need:
        ret = str(a)
    while x >= 9:
        ret += "9"
        x -= 9
    if x > 0:
        ret += str(x)
    return int(ret[::-1])


for N, K in NK:
    if K == 0:
        ans = make(N, 0, False)
    else:
        K += 1
        ans = INF
        for a in range(10):
            P = N - (K-1)*K//2 + 9*max(a+K-10,0)
            if P%K != 0: continue
            P //= K
            P -= a
            if P < 0: continue
            ans = min(ans, make(P, a))
    if ans == INF:
        print(-1)
    else:
        print(ans)