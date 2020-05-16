import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
already = set()
P = []
iszero = False
for a in A:
    a %= M
    if a in already:
        iszero = True
        break
    already.add(a)
    P.append(a)

if iszero:
    print(0)
else:
    ans = 1
    for i, p in enumerate(P):
        for j in range(i+1, len(P)):
            ans = ans * (P[j]-p) % M
    print(ans)