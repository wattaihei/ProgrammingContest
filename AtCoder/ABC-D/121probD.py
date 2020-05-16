A, B = map(int, input().split())

n = A // 2
m = B // 2
if (m-n)%2 == 0:
    c = 0
else:
    c = 1
if B % 2 == 0:
    c = c^B
else:
    c = c^1
if A % 2 == 1:
    c = c^(A-1)
print(c)