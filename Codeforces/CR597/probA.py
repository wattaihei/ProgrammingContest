N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for A, B in AB:
    ok = True
    for n in range(2, max(A,B)+1):
        if A % n == 0 and B % n == 0:
            ok = False
    if ok:
        print('Finite')
    else:
        print('Infinite')