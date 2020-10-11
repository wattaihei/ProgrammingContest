import sys
input = sys.stdin.readline

mod = 10**9+7

N = int(input())
A = list(map(int, input().split()))

s = 0
s2 = 0
for a in A:
    s2 = (s2 + a*a) % mod
    s = (s + a) % mod

ans = (s*s - s2) * pow(2, mod-2, mod) % mod
print(ans)