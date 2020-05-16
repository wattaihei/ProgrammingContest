from bisect import bisect_right
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(lambda x:abs(int(x)), input().split()))

A.sort()

ans = 0
for i in range(N):
    ib = bisect_right(A, A[i]*2)
    ans += ib-i-1
print(ans)