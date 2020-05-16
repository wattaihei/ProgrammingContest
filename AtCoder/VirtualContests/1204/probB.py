N, M, K = map(int, input().split())

ok = False
for n in range(N+1):
    for m in range(M+1):
        if n*m + (N-n)*(M-m) == K:
            ok = True

print("Yes" if ok else "No")