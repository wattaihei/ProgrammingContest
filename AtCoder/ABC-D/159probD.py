import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0
for v in C.values():
    ans += v*(v-1)//2

for a in A:
    v = C[a]
    if v == 1:
        print(ans)
    else:
        print(ans - v*(v-1)//2 + (v-1)*(v-2)//2)