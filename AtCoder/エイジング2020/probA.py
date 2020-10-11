import sys
input = sys.stdin.readline

L, R, d = map(int, input().split())

ans = 0
for n in range(L, R+1):
    if n%d == 0:
        ans += 1
print(ans)