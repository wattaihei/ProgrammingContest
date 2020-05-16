from bisect import bisect_left, bisect_right

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

a = bisect_left(A, X)
b = bisect_right(A, X)
c = min([a, M-a, b, M-b])
print(c)