N = int(input())
A = [int(input()) for _ in range(N)]

B = sorted(A, reverse=True)
ma = B[0]

for i in range(N):
    if A[i] != ma:
        print(ma)
    else:
        print(B[1])