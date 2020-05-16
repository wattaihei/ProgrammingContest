import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for n in range(1, N+1):
    ans += 1/n
print(ans)