from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for a in range(100000):
    k = bisect_right(A, a+2) - bisect_left(A, a)
    ans = max(ans, k)

print(ans)