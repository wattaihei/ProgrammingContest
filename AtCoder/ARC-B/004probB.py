N = int(input())
A = [int(input()) for _ in range(N)]

a1 = sum(A)
m1 = max(A)
if a1 - m1 >= m1:
    a2 = 0
else:
    a2 = 2*m1 - a1
print(a1)
print(a2)