import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


L = 30
ans = 0
for l in range(L):
    P = []
    g = 1<<l
    g2 = 1<<(1+l)
    B1 = []
    B2 = []
    for b in B:
        if b&g:
            B1.append(b)
        else:
            B2.append(b)
    B = B2 + B1

    A1 = []
    A2 = []
    for a in A:
        if a&g:
            A1.append(a)
        else:
            A2.append(a)
    A = A1 + A2

    count = 0
    ind1 = 0
    ind2 = 0
    ind3 = 0
    for a in A:
        while ind1 < N and B[ind1]%g2 + a%g2 < g:
            ind1 += 1
        while ind2 < N and B[ind2]%g2 + a%g2 < 2*g:
            ind2 += 1
        while ind3 < N and B[ind3]%g2 + a%g2 < 3*g:
            ind3 += 1
        count += ind2 - ind1 + N - ind3
    if count%2 == 1:
        ans += g
print(ans)