import sys
input = sys.stdin.buffer.readline
from collections import deque

N = int(input())
P = list(map(int, input().split()))

def nears(n):
    ret = []
    if n%N != 0:
        ret.append(n-1)
    if n%N != N-1:
        ret.append(n+1)
    if n//N != 0:
        ret.append(n-N)
    if n//N != N-1:
        ret.append(n+N)
    return ret

NeedS = []
for p in range(N**2):
    NeedS.append(min([p%N, p//N, N-1-p%N, N-1-p//N]))

isChecked = [False]*(N**2)
ans = 0
for p in P:
    p -= 1
    ans += NeedS[p]
    isChecked[p] = True
    q = deque()
    q.append(p)
    while q:
        p = q.popleft()
        d = NeedS[p]
        if not isChecked[p]: d += 1
        for np in nears(p):
            if d < NeedS[np]:
                NeedS[np] = d
                q.append(np)
print(ans)