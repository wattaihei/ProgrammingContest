import sys
input = sys.stdin.buffer.readline

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    P = []
    Inds = []
    for i, (a, b) in enumerate(zip(A, B)):
        if b == 0:
            P.append(a)
            Inds.append(i)
    P.sort(reverse=True)

    for a, i in zip(P, Inds):
        A[i] = a
    
    print(" ".join(map(str, A)))