N = int(input())
A = list(map(int, input().split()))

mina = 10**10
maxa = -10**10
for i, a in enumerate(A):
    if a < mina:
        l = i+1
        mina = a
    if a > maxa:
        r = i+1
        maxa = a


if maxa <= 0:
    print(N-1)
    for n in range(N, 1, -1):
        print(n, n-1)
elif mina >= 0:
    print(N-1)
    for n in range(1, N):
        print(n, n+1)
else:
    print(2*N-1)
    if abs(maxa) > abs(mina):
        for i in range(1, N+1):
            print(r, i)
        for n in range(1, N):
            print(n, n+1)
    else:
        for i in range(N, 0, -1):
            print(l, i)
        for n in range(N, 1, -1):
            print(n, n-1)