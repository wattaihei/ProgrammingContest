N, M, D = map(int, input().split())
if D == 0:
    print((N-D)*(M-1)/N**2)
else:
    print(2*(N-D)*(M-1)/N**2)