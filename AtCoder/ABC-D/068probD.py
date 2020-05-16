K = int(input())
N = 50

A = []
for k in range(N):
    a = -(K%N)
    if K%N > k:
        a += N+1
    A.append(k + K//N + a)

print(N)
for a in A:
    print(a, end=' ')
print()