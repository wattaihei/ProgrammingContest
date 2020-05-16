from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

CI = []
for b in B:
    ci = bisect_right(C, b)
    CI.append(N-ci)

CII = CI[::-1]
D = []
d = 0
for cii in CII:
    d += cii
    D.append(d)

D = D[::-1]

ans = 0
for a in A:
    bi = bisect_right(B, a)
    if bi == N:
        continue
    ans += D[bi]
print(ans)