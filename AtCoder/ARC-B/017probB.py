import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

UP = []
up = 1
for i in range(1, N):
    if A[i-1] < A[i]:
        up += 1
    else:
        UP.append(up)
        up = 1
UP.append(up)

ans = 0
for u in UP:
    ans += max(0, u-K+1)
print(ans)