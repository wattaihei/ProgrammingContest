import sys
input = sys.stdin.readline

A = [int(input()) for _ in range(6)]
ans = 0
for jac in range(A[3]+1):
    first = min(jac, A[0])
    second = min([A[3]-jac, A[1], A[2]])
    ans = max(ans, first*A[4]+second*A[5])
print(ans)