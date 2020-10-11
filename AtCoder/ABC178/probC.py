N = int(input())

mod = 10**9+7

a9 = 1
a8 = 1
a10 = 1
for _ in range(N):
    a9 = a9 * 9 % mod
    a8 = a8 * 8 % mod
    a10 = a10 * 10 % mod

ans = (a10 - 2*a9 + a8) % mod
print(ans)