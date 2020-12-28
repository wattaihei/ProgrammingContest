import sys
input = sys.stdin.buffer.readline

N, T = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

ans = 0
pre = A[0]
for a in A[1:]:
    ans += min(a-pre, T)
    pre = a
ans += T
print(ans)