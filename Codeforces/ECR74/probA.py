Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for x, y in Query:
    a = x-y
    if a > 1:
        print('YES')
    else:
        print('NO')