import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().rstrip().split())

ans = 0
for n in range(1, 2*N+1):
    am = n-K
    if am < 2: continue
    ans += min(min(n-1, N), max(2*N-n+1, 0)) * min(min(am-1, N), max(2*N-am+1, 0))

print(ans)