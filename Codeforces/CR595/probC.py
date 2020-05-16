import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    A = []
    n = N
    while n > 0:
        A.append(n%3)
        n //= 3

    last2 = -1
    last0 = {}
    for i, a in enumerate(A):
        if a == 2:
            last2 = i
        elif a == 0 and not last2 in last0:
            last0[last2] = i
    if last2 == -1:
        B = A
    else:
        B = []
        if last2 in last0:
            d0 = last0[last2]
            for i in range(len(A)):
                if i < d0:
                    B.append(0)
                elif i == d0:
                    B.append(1)
                else:
                    B.append(A[i])
        else:
            B = [0]*len(A) + [1]
    
    ans = 0
    dig = 1
    for b in B:
        ans += dig*b
        dig *= 3
    print(ans)