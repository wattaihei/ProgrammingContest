N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
elif K == 0:
    print(0)
else:
    l = 0
    r = 0
    X = S[0]
    a = 0
    while l < N and r < N:
        if X > K:
            X //= S[l]
            l += 1
        if X <= K:
            a = max(a, r-l+1)
            r += 1
            if r == N:
                break
            X *= S[r]
    print(a)