A = list(map(int, input().split()))
K = int(input())

A.sort()
for k in range(K):
    A[-1] *= 2
print(sum(A))