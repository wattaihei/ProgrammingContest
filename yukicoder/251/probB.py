import sys
input = sys.stdin.readline

N, K, X, Y = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 0
alr = 1
for i, a in enumerate(A):
    a -= alr
    a = max(a, 0)
    if (N-i)*X < Y:
        ans += ((a+K-1)//K) * X
    else:
        alr += ((a+K-1)//K) * K
        ans += ((a+K-1)//K) * Y
print(ans)