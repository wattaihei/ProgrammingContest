N, P = map(int, input().split())

if N <= P:
    print(-1)
else:
    d = 1
    while True:
        A = N-P*d
        if P > 0 and A <= 0:
            d = -1
            break
        if bin(A).count('1') <= d and A >= d:
            break
        d += 1
    print(d)