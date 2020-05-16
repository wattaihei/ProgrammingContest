M, K = map(int, input().split())

if M == 0:
    if K == 0:
        print(0, 0)
    else:
        print(-1)
elif M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
elif K >= 2**M:
    print(-1)
else:
    A = []
    for i in range(2**M):
        if i == K:
            continue
        A.append(i)
    ans = A[:] + [K] + A[::-1] + [K]
    print(' '.join([str(a) for a in ans]))