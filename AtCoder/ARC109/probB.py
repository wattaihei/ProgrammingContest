from math import sqrt

N = int(input())

p = int(sqrt(2*(N+1)))

k = -1
for m in range(p-1, p+5):
    if m*(m+1) <= 2*(N+1):
        k = m

print(N-k+1)