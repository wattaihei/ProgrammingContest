Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, K in Query:
    step = 0
    while N > 0:
        if N % K == 0:
            N //= K
            step += 1
        else:
            a = N%K
            N -= a
            step += a
    print(step)