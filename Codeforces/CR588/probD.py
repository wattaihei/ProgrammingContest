import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = Counter(A)
ans = 0
P = set(list(range(N)))
for bit, count in C.items():
    if count == 1: continue
    must = []
    for p in P:
        if bit|A[p] == bit:
            must.append(p)
            ans += B[p]
    for p in must:
        P.remove(p)

print(ans)