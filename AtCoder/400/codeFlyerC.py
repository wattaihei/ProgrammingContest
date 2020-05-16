from bisect import bisect_right

N, D = map(int, input().split())
A = list(map(int, input().split()))

c = 0
for i, a in enumerate(A):
    ib = bisect_right(A, a+D)
    print(ib, i, a)
    c += ib-i-1
print(c)