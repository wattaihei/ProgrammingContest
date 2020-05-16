import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = []
for _ in range(N):
    a = sorted(list(input()))
    A.append(''.join(a))

B = Counter(A)

ans = 0
for k,v in B.items():
    ans += v*(v-1)//2
print(ans)