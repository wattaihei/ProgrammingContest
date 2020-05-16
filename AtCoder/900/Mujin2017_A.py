import sys
input = sys.stdin.readline

mod = 10**9+7

N = int(input())
A = list(map(int, input().split()))

i = 0
c = 0
ans = 1
while i < N:
    if 2*c + 1 <= A[i]:
        i += 1
        c += 1
    else:
        ans = ans * (c+1) % mod
        i += 1
for n in range(1, c+1):
    ans = ans * n % mod
print(ans)