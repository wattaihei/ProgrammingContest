A = list(map(int, input().split()))
A.sort()
if A[0]+1 == A[1] and A[1]+1 == A[2] and A[2]+1 == A[3]:
    print("Yes")
else:
    print("No")