N, L, R = map(int, input().split())

a1 = 0
for r in range(R):
    a1 += 2**r
a1 += 2**(R-1)*(N-R)

a2 = 0
for l in range(L):
    a2 += 2**l
a2 += (N-L)
print(a2, a1)