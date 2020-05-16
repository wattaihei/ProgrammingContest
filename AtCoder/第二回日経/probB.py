import sys
input = sys.stdin.readline
from collections import Counter

mod = 998244353

def power_func(a,n,mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

N = int(input())
D = list(map(int, input().split()))

A = Counter(D)
B = sorted(A.items())

if D[0] != 0:
    print(0)
else:
    ans = 1
    for i, (k, num) in enumerate(B):
        if i == 0:
            if num != 1:
                ans = 0
                break
            pre = 0
            continue
        if k != pre + 1:
            ans = 0
            break
        if k == 1:
            pre = 1
            p = num
            continue
        ans = ans * power_func(p, num, mod) % mod
        p = num
        pre = k
    
    print(ans)
    