import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


A.sort()
B.sort()
if N%2 == 1:
    m = A[N//2]; M = B[N//2]
    print(M-m+1)
else:
    m1 = A[N//2-1]; m2 = A[N//2]
    M1 = B[N//2-1]; M2 = B[N//2]
    ans = M1 + M2 - (m1+m2) + 1
    print(ans)