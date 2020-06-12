import sys
input = sys.stdin.buffer.readline


A, B, C, D = map(int, input().split())

tmp = 0
ans = 0
for k in reversed(range(C, B+C+1)):
    if k <= D:
        ans += tmp
    tmp += max(min(B, k-B) - max(A,k-C) + 1, 0)

print(ans)
