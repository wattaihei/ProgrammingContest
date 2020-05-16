S = list(str(int(input())+1))
L = len(S)
mod = int(1E9+7)

n = 0
ans = 0
for i, s in enumerate(S):
    if s == '1':
        ans += ((2**(n%(mod-1)))%mod * (3**((L-i-1)%(mod-1)))%mod) % mod
        ans %= mod
        n += 1
print(ans)