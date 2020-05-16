from bisect import bisect_left

Q = int(input())
data = []
for _ in range(Q):
    N = int(input())
    P = list(map(int, input().split()))
    data.append([N, P])

for N, P in data:
    lok = True
    for i, n in enumerate(P):
        if i == 0:
            pre = n
            if n == N:
                pre = 0
            continue
        if n == N:
            pre = 0
            continue
        if pre + 1 != n:
            lok = False
            break
        pre = n
    
    rok = True
    for i, n in enumerate(P):
        if i == 0:
            pre = n
            if n == 1:
                pre = N+1
            continue
        if n == 1:
            pre = N+1
            continue
        if pre - 1 != n:
            rok = False
            break
        pre = n
    #print(lok, rok)
    if lok or rok:
        print('YES')
    else:
        print('NO')
