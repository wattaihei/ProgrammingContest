import sys
input = sys.stdin.readline
INF = 10**18

N, M = map(int, input().split())
state = [list(input().rstrip()) for _ in range(N)]

T = [[] for _ in range(11)]
for n in range(N):
    for m in range(M):
        s = state[n][m]
        if s == "S":
            T[0].append((n, m))
        elif s == "G":
            T[10].append((n, m))
        else:
            T[int(s)].append((n, m))

dp = [0]
for num in range(10):
    ndp = []
    for (pn, pm) in T[num+1]:
        tmp = INF
        for (n, m), count in zip(T[num], dp):
            tmp = min(tmp, abs(pn-n)+abs(pm-m)+count)
        ndp.append(tmp)
    dp = ndp[:]

if dp[0] >= INF:
    print(-1)
else:
    print(dp[0])