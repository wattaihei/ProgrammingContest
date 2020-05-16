A = list(map(int, input().split()))

A.sort()
if A[0] != A[1]:
    print(A[0])
else:
    print(A[-1])