import sys
input = sys.stdin.readline

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

x = M[0][1]
y = M[1][2]
z = M[2][0]
ans = [None]*N

T = y*z//x
c = int(T**0.5)
C = [c-1, c, c+1, c+2]
for p in C:
    if p*p == T:
        ans[2] = p
        break

ans[0] = z//ans[2]
ans[1] = y//ans[2]

for n in range(3, N):
    ans[n] = M[0][n]//ans[0]

print(*ans)