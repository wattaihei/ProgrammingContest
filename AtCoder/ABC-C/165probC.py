import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

P = []
def dfs(dmax, now):
    if len(now) == N:
        P.append(now)
        return
    for n in range(dmax, M+1):
        dfs(n, now+[n])
dfs(1, [])
ans = 0
for A in P:
    score = 0
    for a, b, c, d in ABCD:
        if A[b-1] - A[a-1] == c:
            score += d
    ans = max(ans, score)

print(ans)