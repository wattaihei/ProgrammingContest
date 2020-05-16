N, K = map(int, input().split())

if K == 0:
    print(N**2)
else:
    ans = 0
    for b in range(K+1, N+1):
        q = N // b
        r = N % b
        if r >= K:
            ans += (r-K+1)*(q+1) + (b-r-1)*q
        else:
            ans += (b-K)*q
    print(ans)