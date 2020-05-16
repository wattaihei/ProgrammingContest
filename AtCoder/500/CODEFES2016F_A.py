import sys
input = sys.stdin.readline

mod = 10**9+7

N = int(input())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(N)]

A.sort(reverse=True)
B.sort(reverse=True)

P = []
while A or B:
    if len(A) == 0:
        b = B.pop()
        P.append(0)
    elif len(B) == 0:
        a = A.pop()
        P.append(1)
    else:
        a = A.pop()
        b = B.pop()
        if a > b:
            P.append(0)
            A.append(a)
        else:
            P.append(1)
            B.append(b)

a = 0
b = 0
ans = 1
for p in P:
    if p == 0:
        if b > 0:
            ans = ans * b % mod
            b -= 1
        else:
            a += 1
    else:
        if a > 0:
            ans = ans * a % mod
            a -= 1
        else:
            b += 1
print(ans)

