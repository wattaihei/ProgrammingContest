from collections import Counter

import sys
input = sys.stdin.readline

S = list(input().rstrip())
A = Counter(S)

P = list(A.values())
ok = True
if len(P) == 2:
    if P[0] == 1 and P[1] == 1:
        ok = True
    else:
        ok = False
elif len(P) == 1:
    if P[0] == 1:
        ok = True
    else:
        ok = False
else:
    P.sort()
    if P[-1] - P[0] > 1:
        ok = False
print("YES" if ok else "NO")