N, X = map(int, input().split())
if N == 2:
    if X != 2:
        print('No')
    else:
        print('Yes')
        print(1)
        print(2)
        print(3)
elif X == 1 or X == 2*N-1:
    print('No')
else:
    print('Yes')
    used = [False]*(2*N-1)
    if X >= N:
        p1 = 2*N-1
        s1 = 1
        s2 = 2
    else:
        p1 = 1
        s1 = 2*N-1
        s2 = 2*N-2
    a = 0
    for k in range(1, 2*N):
        if a == N-2:
            print(s1)
            print(X)
            print(p1)
            print(s2)
            a += 4
        if k in [X, p1, s1, s2]:
            continue
        print(k)
        a += 1
