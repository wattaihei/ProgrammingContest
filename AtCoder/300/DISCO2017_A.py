K = int(input())

L = 300//K
M = 200//K

c = 0
for i in range(-L, L):
    for j in range(-L, L):
        points = [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
        ok = True
        for x, y in points:
            if L%2 == 0 and 4*(x**2 + y**2) > L**2:
                ok = False
            if L%2 == 1 and (2*x-1)**2 + (2*y-1)**2 > L**2:
                ok = False
        if ok:
            c += 1

d = 0
for i in range(-M, M):
    for j in range(-M, M):
        points = [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
        ok = True
        for x, y in points:
            if M%2 == 0 and 4*(x**2 + y**2) > M**2:
                ok = False
            if M%2 == 1 and (2*x-1)**2 + (2*y-1)**2 > M**2:
                ok = False
        if ok:
            d += 1
print(d, c)