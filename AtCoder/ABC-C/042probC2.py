N, K = map(int, input().split())
D = list(map(int, input().split()))

n = N
while True:
    k = str(n)
    ok = True
    for ki in k:
        if int(ki) in D:
            ok = False
    if ok:
        print(n)
        break
    n += 1