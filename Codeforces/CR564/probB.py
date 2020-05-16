import sys
input = sys.stdin.readline

N = int(input())
M = (N+2)//2
print(M)
r, c = 1, 1
for _ in range(N):
    print(r, c)
    if r < M:
        r += 1
    else:
        c += 1