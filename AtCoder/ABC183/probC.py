import sys
input = sys.stdin.buffer.readline

from itertools import permutations

N, K = map(int, input().rstrip().split())

Ts = [list(map(int, input().rstrip().split())) for _ in range(N)]

P = permutations(range(1, N))

ans = 0
for arr in P:
    pre = 0
    time = 0
    for n in arr:
        time += Ts[pre][n]
        pre = n
    time += Ts[pre][0]
    if time == K:
        ans += 1

print(ans)