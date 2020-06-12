LIM = 10**9

A, R, N = map(int, input().split())
if R == 1:
    print(A)
else:
    large = False
    t = A
    for n in range(N-1):
        t *= R
        if t > LIM:
            large = True
            break
    if large:
        print("large")
    else:
        print(t)