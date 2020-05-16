
L = 10**6
P = [-1 for _ in range(L)]

for i in range(1, L):
    n = i
    c = 0
    while n != 1:
        if n < L:
            if P[n] != -1:
                c += P[n]
                break
        c += 1
        if n%2==0:
            n //= 2
        else:
            n = 3*n+1
    P[i] = c

a = 0
for i in range(1, L):
    if P[i] > a:
        a = P[i]
        ans = i
print(ans)