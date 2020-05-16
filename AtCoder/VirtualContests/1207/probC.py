import sys
input = sys.stdin.readline

N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.sort(reverse=True)

l = N-1
c = 0
ans = 0
for i, a in enumerate(A):
    ans += 1
    if a + A[l] + 1 <= C:
        c += 2
        l -= 1
    else:
        c += 1
    if c >= N:
        print(ans)
        break