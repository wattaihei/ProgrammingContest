import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

P = 30

N = int(input())
L = [[[], [], []] for _ in range(P)]
for _ in range(N):
    s = input().rstrip()
    kurai = 0
    if "." in s:
        s1, s0 = s.split(".")
        if int(s0) == 0:
            num = int(s1)
        else:
            num = int(s1+s0)
            kurai = len(s0)
    else:
        num = int(s)
    while num % 10 == 0:
        num //= 10
        kurai -= 1
    
    k2 = 0
    while num%2 == 0:
        num //= 2
        k2 += 1
    k5 = 0
    while num%5 == 0:
        num //= 5
        k5 += 1
    if k2 > 0:
        L[kurai][0].append(k2)
    elif k5 > 0:
        L[kurai][1].append(k5)
    else:
        L[kurai][2].append(0)

for p in range(P):
    for i in range(3):
        L[p][i].sort()


def bis(List, n):
    return len(List) - bisect_left(List, n)

ans = 0
for i in range(P):
    if i >= 10:
        i -= P
    for j in range(P):
        if j >= 10: j -= P
        if i < j: continue
        r = i+j
        
        if r <= 0:
            i3 = len(L[i][0]) + len(L[i][1]) + len(L[i][2])
            j3 = len(L[j][0]) + len(L[j][1]) + len(L[j][2])
            if i3 > 0 and j3 > 0:
                ans += i3*j3 if i != j else (i3-1)*i3//2
        else:
            if i != j:
                i1 = bis(L[i][0], r)
                j1 = bis(L[j][1], r)
                ans += i1*j1

                i2 = bis(L[i][1], r)
                j2 = bis(L[j][0], r)
                ans += i2*j2
            else:
                i1 = bis(L[i][0], r)
                j1 = bis(L[j][1], r)
                ans += i1*j1

print(ans)