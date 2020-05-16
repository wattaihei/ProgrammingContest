N = int(input())
A = list(map(int, input().split()))

ans = 0
for j in range(N):
    B = A[j:]
    aoki = 0
    for i in range(j):
        S = 0
        D = A[i:j]
        for k, d in enumerate(D):
            if k % 2 == 0:
                continue
            S += d
        if S > aoki:
            aoki = S
            ind = i
    S = 0
    for i in range(N-j):
        if i % 2 == 0:
            continue
        S += B[i]
        if S > aoki:
            aoki = S
            ind = i + j
        print(i, S)
    if ind < j:
        C = A[ind:j]
    else:
        print(ind)
        if ind % 2 == 1:
            C = B[:ind+1]
        else:
            C = B[:ind]
    tak = 0
    for i, c in enumerate(C):
        if i % 2 == 0:
            tak += c
    ans = max(ans, tak)
    print(C, aoki, tak)

print(ans)