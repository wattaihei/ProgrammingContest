import sys
input = sys.stdin.readline
mod = 998244353

N = int(input())

A = [10, 180]
a = 180
t = 81
for _ in range(N-2):
    t = t*10%mod
    a = (10*a+t)%mod
    A.append(a)
if N == 1:
    A = [10]
print(*A[::-1])