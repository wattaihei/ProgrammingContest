import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X = [int(input())-1 for _ in range(M)]

l = -1
r = N*2

while r - l > 1:
    m = (l+r)//2
    ok = True
    pre = -1
    for x in X:
        d = x-pre-1
        if d > m:
            ok = False
            break
        if d > 0:
            to = max([m-2*d, (m-d)//2, 0])
            pre = x + to
        else:
            pre = x + m
    if pre < N-1:
        ok = False

    if ok:
        r = m
    else:
        l = m

print(r)