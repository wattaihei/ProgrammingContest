import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ok = True
for v in C.values():
    if v != 1:
        ok = False
        break
print("YES" if ok else "NO")