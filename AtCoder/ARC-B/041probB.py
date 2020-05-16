import sys
input = sys.stdin.readline

N, M = map(int, input().split())
state = [[int(a) for a in list(input().rstrip())] for _ in range(N)]

ans = [[0]*M for _ in range(N)]
for h in range(N):
    for w in range(M):
        if state[h][w] == 0: continue
        if h == 0:
            ans[h][w] = state[h][w]
        