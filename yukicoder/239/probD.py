import sys
input = sys.stdin.readline

mod = 10**9+7
N = int(input())
A = [[], []]
for _ in range(N):
    t, x = map(int, input().split())
    A[t].append(x)

A[0].sort()
A[1].sort(reverse=True)

ans = 1
for l, a in enumerate(A[0]):
    ans = ans * max(a-l, 0) % mod

for r, a in enumerate(A[1]):
    ans = ans * max(min(N-a+1, len(A[1]))-r, 0) % mod

print(ans)