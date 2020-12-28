import sys
input = sys.stdin.buffer.readline
from collections import deque

N = int(input())
A = list(map(int, input().rstrip().split()))

n = 0
S = deque()
ans = []
ok = True
for i, a in enumerate(A):
    if a == n+1:
        ans.append((i, len(S)))
        n += 1
        while S:
            p = S.popleft()
            if p == n+1:
                n += 1
            else:
                S.appendleft(p)
                break
    else:
        S.append(a)

P = []
for i, l in ans:
    for j in range(l):
        P.append(i-j)
    if len(P) > N-1:
        ok = False
        break



Q = sorted(P)
for i, p in enumerate(Q):
    if i+1 != p:
        ok = False
        break

if len(P) != N-1:
    ok = False

if n != N or not ok:
    print(-1)
else:
    print(*P, sep="\n")