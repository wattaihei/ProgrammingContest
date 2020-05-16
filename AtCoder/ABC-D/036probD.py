import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


N = int(input())
mod = int(1E9+7)
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dp = [[1, 1] for _ in range(N)]

def dfs(p, pv):
    for np in graph[p]:
        if np == pv:
            continue
        dfs(np, p)
        dp[p][1] = (dp[p][1] * dp[np][0]) % mod
        dp[p][0] = dp[p][0] * (dp[np][0] + dp[np][1]) % mod
    return

dfs(0, -1)
#print(dp)
s = (dp[0][0] + dp[0][1]) % mod
print(s)