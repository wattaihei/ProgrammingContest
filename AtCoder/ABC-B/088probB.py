N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
l = 0
r = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        l += a
    else:
        r += a
print(l-r)