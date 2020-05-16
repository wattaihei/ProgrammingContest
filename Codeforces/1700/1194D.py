T = int(input())
Query = [list(map(int, input().split())) for _ in range(T)]

for N, K in Query:
    if K % 3 != 0:
        if N % 3 == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        A = K // 3 - 1
        cycle = 3*A + 4
        N %= cycle
        if N % 3 == 0 and N != cycle - 1:
            print('Bob')
        else:
            print('Alice')
