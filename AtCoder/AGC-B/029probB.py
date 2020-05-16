import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A.sort()
C = Counter(A)

ans = 0
for i in reversed(range(N)):
    a = A[i]
    inv = 2**(a.bit_length())-a
    if a == inv:
        if C[a] >= 2:
            C[a] -= 2
            ans += 1
    elif inv in C.keys():
        if C[inv] >= 1 and C[a] >= 1:
            C[a] -= 1
            C[inv] -= 1
            ans += 1

print(ans)    
