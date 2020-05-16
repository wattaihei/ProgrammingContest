mod = 10**9+7

# modを取りながらべき乗する
def power_func(a,n,mod=mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

N = input()
up = True
M = ''
for l in range(len(N)):
    if up:
        if N[len(N)-l-1] == '0':
            M += '1'
            up = False
        else:
            M += '0'
    else:
        M += N[len(N)-l-1]
if up:
    M += '1'
M = M[::-1]
L = len(M)

c = 0
ans = 0
for l in range(L):
    if int(M[l]) == 1:
        ans += power_func(3, L-l-1) * power_func(2, c) % mod
        c += 1
        ans %= mod

print(ans)