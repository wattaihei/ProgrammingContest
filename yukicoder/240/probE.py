import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

sl = 0
l = K-2
while l >= 0:
    sl += A[l]
    if A[l] < 2:
        break
    l -= 1

sr = 0
r = K
while r < N:
    sr += A[r]
    if A[r] < 2:
        break
    r += 1

if A[K-1] == 0:
    ans = 0
elif A[K-1] == 1:
    ans = max(sl ,sr) + 1
else:
    ans = sl + sr + A[K-1]

print(ans)