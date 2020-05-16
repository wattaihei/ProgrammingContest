N, K = map(int, input().split())
A = list(map(int, input().split()))

def to_rem(A):
    C = []
    for n in range(N):
        if n == 0:
            if A[0] > A[1]:
                C.append(A[0] - A[1])
        elif n == N-1:
            if A[N-1] > A[N-2]:
                C.append(A[N-1]-A[N-2])
        else:
            