N = int(input())

ans = N
for A in range(1, N):
    B = N - A
    Asum = sum([int(a) for a in list(str(A))])
    Bsum = sum([int(b) for b in list(str(B))])
    ans = min(Asum+Bsum, ans)
print(ans)