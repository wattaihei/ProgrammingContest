N = int(input())
A = list(map(int, input().split()))

mod = 998244353

L = len(str(A[0]))
ans = 0
for l in range(L):
    n = 0
    for a in A:
        n += int(str(a)[L-1-l])
    b = (10**(2*l) + 10**(2*l+1)) % mod
    ans = (ans + n*b) % mod
ans = ans * N % mod
print(ans)