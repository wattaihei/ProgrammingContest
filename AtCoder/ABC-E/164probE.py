import sys
input = sys.stdin.readline
import heapq as hp

AM = 50*50+1
INF = 10**15

N, M, S = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, a, b = map(int, input().split())
    graph[u-1].append((a, b, v-1))
    graph[v-1].append((a, b, u-1))
C = []
D = []
for _ in range(N):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

# dp[n][cost] := cost でいけるnの最短
dp = [[INF]*(AM+1) for _ in range(N)]
dp[0][min(AM, S)] = 0
q = [(0, min(AM, S), 0)]
while q:
    dis, cost, p = hp.heappop(q)
    if dp[p][cost] < dis:
        continue
    if 0 <= cost+C[p] <= AM and dp[p][cost+C[p]] > dp[p][cost]+D[p]:
        dp[p][cost+C[p]] = dp[p][cost] + D[p]
        hp.heappush(q, (dp[p][cost+C[p]], cost+C[p], p))
    for a, b, np in graph[p]:
        if 0 <= cost-a <= AM and dp[np][cost-a] > dp[p][cost] + b:
            dp[np][cost-a] = dp[p][cost]+b
            hp.heappush(q, (dp[np][cost-a], cost-a, np))

for n in range(1, N):
    print(min(dp[n]))