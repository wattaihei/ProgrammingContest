import math

N = int(input())

S = []
for n in range(2, int(math.sqrt(N))+1):
    if N % n == 0:
        if N//n > n:
            S.append(n)
            S.append(N//n)
        elif N//n == n:
            S.append(n)
if len(S) == 0:
    print(N)
else:
    S.sort()
    ok = True
    for s in S:
        if s == S[0]: continue
        if s % S[0] != 0:
            ok = False
            break
    if not ok:
        print(1)
    else:
        print(S[0])