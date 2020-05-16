Q = int(input())
Qs = []
for _ in range(Q):
    n, a, b = map(int, input().split())
    s = input()
    Qs.append([n, a, b, s])

for n, a, b, S in Qs:
    l = 0
    L = []
    for s in list(S):
        if s == '0':
            l += 1
        else:
            if not L:
                L.append(l)
            elif l >= 2:
                L.append(l)
            l = 0
    L.append(l)
    if len(L) == 1:
        ans = a*n + b*(n+1)
    else:
        ans = a*(n+2) + b*(2*(n+1)-L[0]-L[-1])
        maxl = len(L)
        for i, l in enumerate(L):
            if i == 0 or i == maxl-1:
                continue
            if (l-1)*b > 2*a:
                ans = ans + 2*a - (l-1)*b
    print(ans)