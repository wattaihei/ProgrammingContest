N = int(input())
A = [int(input()) for _ in range(N)]

A.sort()

if N%2 == 0:
    l = N//2
    B1 = A[:l]
    B2 = A[l:]
    ans = 0
    for i in range(l):
        ans += (B2[i] - B1[i])*2
    ans -= B2[0] - B1[-1]
    print(ans)
else:
    l = N//2
    B1 = A[:l]
    B2 = A[l:]
    a1 = 0
    for i in range(l):
        a1 -= B1[i]*2
    for i in range(l+1):
        if i == 0 or i == 1:
            a1 += B2[i]
        else:
            a1 += B2[i]*2
    
    C1 = A[:l+1]
    C2 = A[l+1:]
    a2 = 0

    for i in range(l):
        a2 += C2[i]*2
    for i in range(l+1):
        if i == l-1 or i == l:
            a2 -= C1[i]
        else:
            a2 -= C1[i]*2
    print(max(a1, a2)) 