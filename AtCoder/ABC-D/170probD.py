import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A.sort()

C = Counter(A)
cannot = set()
L= max(A)
ans = 0
for a in A:
    if a in cannot: continue
    if C[a] == 1:
        ans += 1
    ind = 1
    while a*ind <= L:
        cannot.add(a*ind)
        ind += 1

print(ans)