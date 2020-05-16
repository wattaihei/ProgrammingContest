import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

ans = 0
for i in range(60):
    p = 0
    q = 0
    for a in A:
        if a & (1<<i):
            p += 1
        else:
            q += 1
    ans = (ans + ((1<<i) %mod * p * q) % mod) % mod
print(ans)