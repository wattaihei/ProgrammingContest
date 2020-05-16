import sys
input = sys.stdin.readline

mod = 998244353

n, m, l, r = map(int, input().split())
if n*m % 2 == 1:
    ans = pow(r-l+1, n*m, mod)
else:
    if (r-l+1)%2== 0:
        a = (r-l+1)//2
        b = a
    else:
        a = (r-l+2)//2
        b = (r-l+1)//2
    ans = (pow(a-b, n*m, mod) + pow(a+b, n*m, mod)) * pow(2, mod-2, mod) % mod
print(ans)