N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()
ans = 0
if N%2==0:
    B1 = A[:N//2]
    B2 = A[N//2:]
    ans = 2*(sum(B2)-sum(B1)) + B1[-1] - B2[0]
else:
    B1 = A[:N//2]
    B2 = A[N//2:]
    p = 2*(sum(B2)-sum(B1)) - B2[0] - B2[1]

    C1 = A[:N//2+1]
    C2 = A[N//2+1:]
    q = 2*(sum(C2)-sum(C1)) + C1[-1] + C1[-2]
    ans = max(p, q)

print(ans)