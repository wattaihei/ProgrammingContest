from bisect import bisect_right
import sys
input = sys.stdin.readline


X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

A1 = [A[0]-a for a in A]
B1 = [B[0]-b for b in B]
C1 = [C[0]-c for c in C]

'''
for ia, a in enumerate(A1):
    ib = bisect_right(B1, a)
    ic = bisect_right(C1, a)
    if (ia)*(ib)*(ic) > K:
        break

if ia == X-1:
    A2 = A1
else:
    A2 = A1[:ia+2]
if ib == Y-1:
    B2 = B1
else:
    B2 = B1[:ib+2]
if ic == Z-1:
    C2 = C1
else:
    C2 = C1[:ic+2]
'''
Q = []
for ia, a in enumerate(A1):
    for ib, b in enumerate(B1):
        for ic, c in enumerate(C1):
            if (ia+1) * (ib+1) * (ic+1) > K:
                break 
            Q.append(a+b+c)
Q.sort()
S = A[0] + B[0] + C[0]
for i in range(K):
    print(S-Q[i])