from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        g = A[i]
    else:
        g = gcd(g, A[i])

print(g)