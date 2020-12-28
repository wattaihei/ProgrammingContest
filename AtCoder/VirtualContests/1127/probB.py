import sys
input = sys.stdin.buffer.readline

INF = 10**18

N, Z, W = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

ans = abs(A[-1]-W)
if N > 1:
    ans = max(ans, abs(A[-1]-A[-2]))
print(ans)