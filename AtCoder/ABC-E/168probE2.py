import sys
input = sys.stdin.readline
import math

mod = 10**9+7

N = int(input())
As = {}
Empty = 0
for _ in range(N):
    x, y = map(int, input().split())
    g = math.gcd(x, y)
    if g == 0:
        Empty += 1
        continue
    x, y = x//g, y//g
    if y < 0 or (y==0 and x < 0):
        y = -y
        x = -x
    if (x, y) in As:
        As[(x, y)] += 1
    else:
        As[(x, y)] = 1

ans = 1
for (x, y), num in As.items():
    if (-y, x) in As:
        ans = (ans * (pow(2, num, mod) + pow(2, As[(-y, x)], mod) - 1)) % mod
    elif not (y, -x) in As:
        ans = (ans * pow(2, num, mod)) % mod

print((ans-1+Empty)%mod)