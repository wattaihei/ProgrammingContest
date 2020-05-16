K = int(input())
A = list(map(int, input().split()))


if K == 1:
    if A[0] == 2:
        print(2, 3)
    else:
        print(-1)
else:
    M = 2
    L = 2
    ok = True
    for i in range(K-1, -1, -1):
        a = A[i]
        nM = (M//a)*a
        if M%a != 0:
            nM += a
        nL = (L//a)*a + a - 1
        if nM >= M + a or nM > nL:
            ok = False
            break
        
        L, M = nL, nM
        #print(L, M, a, b)

    if not ok:
        print(-1)
    else:
        print(M, L)