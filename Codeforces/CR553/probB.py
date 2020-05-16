import sys
input = sys.stdin.readline

N, M = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(N)]

ok = False
for b in range(10):
    L1 = [None]*N
    L0 = [None]*N
    for m in range(M):
        for n in range(N):
            if state[n][m] & (1 << b):
                L1[n] = m+1
            else:
                L0[n] = m+1

    must = 0
    leave = 0
    for n in range(N):
        if L0[n] is None:
            must += 1
        elif not L1[n] is None:
            leave += 1
    if leave > 0 or must % 2 == 1:
        leave += must
        ok = True
        L = []
        for n in range(N):
            if not L0[n] is None and not L1[n] is None:
                if leave % 2 == 0:
                    L.append(L0[n])
                    leave -= 1
                else:
                    L.append(L1[n])
            elif L0[n] is None:
                L.append(L1[n])
            else:
                L.append(L0[n])
        break


if ok:
    print("TAK")
    for l in L:
        print(l, end=" ")
    print()
else:
    print("NIE")