N = 100
S = set()
for n in range(1, N+1):
    if n in S: continue
    m = n
    while True:
        m += 1
        if m in S: continue
        k = m^n
        if k in S: continue
        print(n, m, k)
        S.add(n)
        S.add(m)
        S.add(k)
        break
