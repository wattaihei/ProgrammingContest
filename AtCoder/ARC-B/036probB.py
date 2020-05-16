import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

if N == 1:
    print(1)
else:
    B = [0]
    for i in range(1, N-1):
        if A[i-1] > A[i] and A[i] < A[i+1]:
            B.append(i)
    B.append(N-1)
    ans = 0
    for i in range(len(B)-1):
        ans = max(ans, B[i+1]-B[i]+1)
    print(ans)