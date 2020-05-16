N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

F = []
S = []
for i in range(3):
    if A[i] > B[i]:
        S.append((B[i], A[i]))
    elif A[i] < B[i]:
        F.append((A[i], B[i]))

def solve_3(L):
    c = N
    for i in range(N+1):
        if i*L[0][0] > N: break
        for j in range(N+1):
            r = N - i*L[0][0] - j*L[1][0]
            if r < 0: break
            k = r // L[2][0]
            c = max(c, i*L[0][1]+j*L[1][1]+k*L[2][1]+r-L[2][0]*k)
    return c


ans = N
if len(F) == 3:
    ans = solve_3(F)
elif len(S) == 3:
    ans = solve_3(S)
elif len(F) == 2:
    c = N
    for i in range(N+1):
        if i*F[0][0] > N: break
        j = (N - i*F[0][0])//F[1][0]
        c = max(c, i*F[0][1]+j*F[1][1]+N-i*F[0][0]-j*F[1][0])
    if len(S) == 1:
        c = c//S[0][0] * S[0][1] + c%S[0][0]
    ans = c
elif len(F) == 1:
    c = N//F[0][0]*F[0][1] + N%F[0][0]
    if len(S) == 1:
        c = c//S[0][0]*S[0][1] + c%S[0][0]
    elif len(S) == 2:
        r1 = c//S[0][0]*S[0][1] + (c%S[0][0])//S[1][0]*S[1][1] + (c%S[0][0])%S[1][0]
        r2 = c//S[1][0]*S[1][1] + (c%S[1][0])//S[0][0]*S[0][1] + (c%S[1][0])%S[0][0]
        c = max([c, r1, r2])
    ans = c

print(ans)