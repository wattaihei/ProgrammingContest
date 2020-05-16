A,B,C,D,E,F = map(int, input().split())

L = []
for a in range(31):
    for b in range(31):
        k = A*a+B*b
        if 0 < 100*k <= F:
            L.append(k)

L.sort()


su = 0
for i, l in enumerate(L):
    limit = min(F-100*l, E*l)
    wd = 100*l
    if i == 0:
        w = wd
    for c in range(3000):
        if C*c >limit:
            break
        d = (limit - C*c) // D
        p = C*c+D*d
        if p*w > wd*su:
            w = wd
            su = p
print(w+su, su)