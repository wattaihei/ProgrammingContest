N = int(input())

c = 0
for n in range(N):
    for m in range(N):
        points = [(n, m), (n+1, m), (n, m+1), (n+1, m+1)]
        ok = True
        for x, y in points:
            if 2*y > 2*x + N or 2*y < -2*x + N or 2*y < 2*x-N or 2*y > -2*x+3*N:
                ok = False
        if ok:
            c += 1
print(c)