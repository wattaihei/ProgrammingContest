import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

border = sum(A)

c = 0
for a in A:
    if border <= a*4*M:
        c += 1

print("Yes" if c >= M else "No")