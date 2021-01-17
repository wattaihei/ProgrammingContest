import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().rstrip().split())
has = [[False, False] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    a -= 1; b -= 1
    if b == 0 or b == N-1:
        a, b = b, a
    if a == 0:
        has[b][0] = True
    if a == N-1:
        has[b][1] = True

ok = False
for i in range(N):
    if has[i][0] and has[i][1]:
        ok = True
        break

print("POSSIBLE" if ok else "IMPOSSIBLE")