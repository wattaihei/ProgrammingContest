from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = deque([])

for i, a in enumerate(A):
    if i % 2 == 0:
        B.append(a)
    else:
        B.appendleft(a)

C = list(B)
if N % 2 == 1:
    C = C[::-1]

for c in C:
    print(c, end=' ')
print()