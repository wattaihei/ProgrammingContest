import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

pre = -1
P = []
tmp = 0
for i,a in enumerate(A):
    if a > pre:
        P.append(tmp)
    else:
        tmp = i
        P.append(i)
    pre = a

Q = [-1]*N
tmp = N-1
pre = N-1
for i in reversed(range(N)):
    a = A[i]
    if a < pre:
        Q[i] = tmp
    else:
        tmp = i
        Q[i] = tmp
    pre = a

ans = max(Q[0]+1, N-P[N-1])
for i in range(1, N-1):
    ans = max(ans, Q[i]-P[i]+1)
    if A[i-1] < A[i+1]:
        ans = max(ans, Q[i+1]-P[i-1])
print(ans)