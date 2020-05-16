N, M = map(int, input().split())
mod = int(1E9+7)

if abs(N-M) > 1:
    ans = 0
elif N == M:
    n = 1
    for i in range(1, N+1):
        n = n*i % mod
    ans = 2 * n * n % mod
else:
    n = 1
    for i in range(1, N+1):
        n = n*i % mod
    m = 1
    for i in range(1, M+1):
        m = m*i % mod
    ans = n * m % mod

print(ans)