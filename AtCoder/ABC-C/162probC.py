from math import gcd

K = int(input())

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            p = gcd(a, b)
            ans += gcd(p, c)
print(ans)