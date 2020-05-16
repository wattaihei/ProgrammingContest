N = int(input())
P = list(map(int, input().split()))
L = 2*N

for i in range(1, N+1):
    print(i*L, end=' ')
print()

B = [L*(N-i) for i in range(1, N+1)]
for i, p in enumerate(P):
    B[p-1] += i+1
print(' '.join([str(a) for a in B]))