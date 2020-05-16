import sys
input = sys.stdin.readline

N = int(input())

A = len(str(N))
ans = 0

for a in range(A-1):
    if a % 2 != 0:
        continue
    ans += 9*10**a

if A % 2 != 0:
    ans += N - 10**(A-1) + 1
print(ans)