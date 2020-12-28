import sys
input = sys.stdin.buffer.readline

H, Q = map(int, input().rstrip().split())
S = [list(map(int, input().rstrip().split())) for _ in range(H)]

t = 100
for A in S:
    for a in A:
        t = min(a, t)

ans = 0
for A in S:
    for a in A:
        ans += a-t

print(ans)