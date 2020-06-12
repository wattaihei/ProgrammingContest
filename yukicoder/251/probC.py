import sys
input = sys.stdin.readline
from collections import Counter

N, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

C = Counter(A)
ans = 0
if X == 0:
    for c, num in C.items():
        ans += num*(num-1)//2
else:
    for c, num in C.items():
        b = c ^ X
        if b in C:
            ans += C[b]*num

    ans //= 2
print(ans)