import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N%2 == 0:
    ans = min(N//2, K+1)
else:
    ans = min(N, K+1)
print(ans)