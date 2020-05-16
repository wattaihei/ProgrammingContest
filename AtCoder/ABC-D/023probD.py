import sys
input = sys.stdin.readline

N = int(input())
HS = [list(map(int, input().split())) for _ in range(N)]

l = 0
r = 10**14+1
while r-l > 1:
    m = (l+r)//2
    A = [0]*N
    ok = True
    for h, s in HS:
        if h > m:
            ok = False
            break
        k = (m-h)//s
        if k >= N:
            k = N-1
        A[k] += 1
    if not ok:
        l = m
    else:
        t = 0
        for i, a in enumerate(A):
            t += a
            if t > i+1:
                ok = False
                break
        if not ok:
            l = m
        else:
            r = m

print(r)