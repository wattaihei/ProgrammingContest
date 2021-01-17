import sys
input = sys.stdin.buffer.readline
from bisect import bisect_right, bisect_left

INF = 1

N, K = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
A.sort()

Box = [-INF]*K
for a in A:
    i = bisect_left(Box, a)
    if i > 0 and Box[i-1] == a-1:
        Box[i-1] = a

ans = 0
for b in Box:
    if b != -INF:
        ans += b+1
print(ans)