N = int(input())
A = list(map(int, input().split()))
A.sort()

if sum(A[:N]) == sum(A[N:]):
    print(-1)
else:
    print(' '.join([str(a) for a in A]))