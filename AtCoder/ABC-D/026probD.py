from math import sin, pi

A, B, C = map(int, input().split())

def f(t):
    return A*t + B*sin(C*pi*t)

n = 0
while True:
    L = [f(n*A/2/C), f((n+1)*A/2/C)]
    if min(L) <= 100 < max(L):
        break
    n += 1

l = n*A/2/C
r = (n+1)*A/2/C
if f(l) < f(r):
    while abs(f(r)-100) > 1E-7 or abs(f(l)-100) > 1E-7:
        m = (l+r)/2
        if f(m) > 100:
            r = m
        else:
            l = m
else:
    while abs(f(r)-100) > 1E-7 or abs(f(l)-100) > 1E-7:
        m = (l+r)/2
        if f(m) < 100:
            r = m
        else:
            l = m
print(m)