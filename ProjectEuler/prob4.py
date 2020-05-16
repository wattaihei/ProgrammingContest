
A = []
for x in range(100, 1000):
    for y in range(x, 1000):
        n = x * y
        a = str(n)
        l = len(a)
        ok = True
        for i in range(l):
            if a[i] != a[l-i-1]:
                ok = False
        if ok:
            A.append(n)
print(max(A))