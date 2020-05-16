import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
state = [[int(a) for a in list(input().rstrip())] for _ in range(N)]
Query = [list(map(int, input().split())) for _ in range(Q)]
updown = [[0]*(M+1) for _ in range(N)]
for h in range(N-1):
    st = 0
    for w in range(M):
        if state[h][w] and state[h+1][w]:
            st += 1
        updown[h+1][w+1] = st

rileft = [[0]*M for _ in range(N+1)]
for w in range(M-1):
    st = 0
    for h in range(N):
        if state[h][w] and state[h][w+1]:
            st += 1
        rileft[h+1][w+1] = st

dp = [[0]*(M+1) for _ in range(N+1)]
for h in range(N):
    have = False
    connected = 0
    for w in range(M):
        if state[h][w]:
            if not have:
                connected += 1
                have = True
        else:
            if have:
                have = False
        dp[h+1][w+1] = dp[h][w+1] + connected - updown[h][w+1]

for n1, m1, n2, m2 in Query:
    midcon = dp[n2][m2] - dp[n1-1][m2] + updown[n1-1][m2]
    lecon = dp[n2][m1-1] - dp[n1-1][m1-1] + updown[n1-1][m1-1]
    ans = midcon - lecon + (rileft[n2][m1-1] - rileft[n1-1][m1-1])
    print(ans)