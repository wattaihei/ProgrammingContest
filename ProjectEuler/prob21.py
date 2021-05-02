from math import sqrt

def su(n):
    P = set()
    for m in range(1, int(sqrt(n))+2):
        if n%m == 0:
            P.add(n//m)
            P.add(m)
    return sum(P) - n

N = 10000
L = [-1]*(N+1)
ans = 0
for n in range(1, N+1):
    s = su(n)
    if s < n and L[s] == n:
        ans += s + n
    L[n] = s

print(ans)