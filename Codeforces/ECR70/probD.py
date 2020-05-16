import sys
input = sys.stdin.readline
from bisect import bisect_right

Q = int(input())
Query = [int(input()) for _ in range(Q)]

A = [0]
for t in range(1, 10**5):
    A.append(A[-1]+t)

for n in Query:
    NUMs = []
    while n:
        i = bisect_right(A, n)
        NUMs.append(i)
        n -= A[i-1]
    ans = "1"
    now = 0
    while NUMs:
        p = NUMs.pop()
        ans += "3"*(p-now) + "7"
        now = p
    print(ans)