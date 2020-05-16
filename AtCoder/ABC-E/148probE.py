N = int(input())

if N%2 == 1:
    print(0)
else:
    N //= 2
    a = 0
    q = 5
    while q <= N:
        a += N//q
        q *= 5
    print(a)
