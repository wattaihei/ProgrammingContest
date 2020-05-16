N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = int(1E9+7)

C = []
for i in range(N-1):
    a = A[i]
    p = 0
    for j in range(i+1, N):
        if A[j] < a:
            p += 1
    C.append(p)
C.append(0)

D = []
for i in range(N):
    a = A[i]
    q = 0
    for j in range(N):
        if A[j] < a:
            q += 1
    D.append(q)

ans = 0
for i in range(N):
    ans += C[i]*K + D[i]*K*(K-1)//2
    ans = ans % mod
print(ans)