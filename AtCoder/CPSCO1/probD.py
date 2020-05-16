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

N = int(input())
print(power_func(5, N-1)*8%mod)