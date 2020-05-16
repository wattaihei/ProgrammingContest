import sys
input = sys.stdin.readline
from collections import Counter

Q = int(input())
Query = []
for _ in range(Q):
    S = list(input().rstrip())
    T = list(input().rstrip())
    Query.append((S, T))

for S, T in Query:
    Cs = Counter(S)
    Ct = Counter(T)
    ok = False
    for k in Cs.keys():
        if k in Ct:
            ok = True
            break
    print("YES" if ok else "NO")