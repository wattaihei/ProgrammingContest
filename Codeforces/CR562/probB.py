import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

B = [[] for _ in range(N)]
for i, (a1, a2) in enumerate(A):
    B[a1].append(i)
    B[a2].append(i)

over = []
for num in range(N):
    if len(B[num]) >= 3:
        over.append(num)

if len(over) >= 3:
    ans = "NO"
elif len(over) == 2:
    ans = "YES"
    for a1, a2 in A:
        if not a1 in over and not a2 in over:
            ans = 'NO'
            break
elif len(over) == 1:
    x = over[0]
    to_check = [True]*M
    for ind in B[x]:
        to_check[ind] = False
    C = []
    for ind in range(M):
        if to_check[ind]:
            C.append(ind)
    if len(C) >= 3:
        ans = 'NO'
    elif len(C) == 2:
        i0, i1 = C
        a0, b0 = A[i0]
        if a0 in A[i1] or b0 in A[i1]:
            ans = 'YES'
        else:
            ans = 'NO'
    else:
        ans = 'YES'
else:
    if len(A) >= 5:
        ans = 'NO'
    else:
        prob = set()
        for a, b in A:
            prob.add(a)
            prob.add(b)
        P = list(prob)
        l = len(P)
        ans = 'NO'
        for i in range(l-1):
            for j in range(i, l):
                X = [P[i], P[j]]
                ok = True
                for a1, a2 in A:
                    if not a1 in X and not a2 in X:
                        ok = False
                if ok:
                    ans = 'YES'

print(ans)