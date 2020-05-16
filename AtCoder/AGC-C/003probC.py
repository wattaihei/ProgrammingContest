import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

B0 = set()
for i in range(N):
    if i % 2 == 0:
        B0.add(A[i])

A.sort()

ans = 0
for i in range(N):
    if i%2 == 0:
        if not A[i] in B0:
            ans += 1

print(ans)