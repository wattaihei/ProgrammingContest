import sys
input = sys.stdin.readline

K, Q = map(int, input().split())
D = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, x, mod in Query:
    Td = []
    for d in D:
        Td.append(d%mod)
    Init = [0]
    zero_count = 0
    zero_tmp = 0
    for i, d in enumerate(Td):
        Init.append(Init[-1]+d)
        if d == 0:
            zero_count += 1
            if i < (n-1)%K:
                zero_tmp += 1
    c = Init.pop()
    last = x + c*((n-1)//K) + Init[(n-1)%K]
    over_count = last//mod - x//mod
    print((n-1)-over_count-zero_count*((n-1)//K)-zero_tmp)
        