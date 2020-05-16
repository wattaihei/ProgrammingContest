import sys
input = sys.stdin.readline
mod = 10**9+7

N, M = map(int, input().split())

tmp = 0
for i in range(1, M+1):
    tmp = (pow(i, N, mod) - tmp )
print(ans)