import sys
input = sys.stdin.readline
INF1 = 10**6
INF2 = 10**17

N, M = map(int, input().split())
A = list(map(int, input().split()))
XW = [list(map(int, input().split())) for _ in range(M)]
XW.sort()

l = 0
r = INF1
while r-l > 1:
    c = (l+r)//2
    Left_min = [INF2]
    for i, a in enumerate(A):
        Left_min.append(min(Left_min[-1], a-c*(i+1)))
    Right_min = [INF2]
    for i in reversed(range(N)):
        Right_min.append(min(Right_min[-1], A[i]+c*(i+1)))
    
    ok = True
    for x, w in XW:
        if w-c*x >= Left_min[x-1] or w+c*x >= Right_min[N+1-x]:
            ok = False
    if c == 1:
        print(Left_min)
        print(Right_min)
        
    if ok:
        r = c
    else:
        l = c
 
if r == INF1:
    print(-1)
else:
    print(r)