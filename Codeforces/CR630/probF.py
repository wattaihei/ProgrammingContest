import sys
input = sys.stdin.readline

mod = 998244353

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dp = [[1, 1, 2] for _ in range(N)]
stack = [0]
Ind = [0]*N
while stack:
    p = stack[-1]
    if Ind[p] == len(graph[p]):
        stack.pop()

        if stack:
            if Ind[p] == 1:
                dp[p][2] = 0
            par = stack[-1]
            dp[par][1] = (dp[par][1] * (2*dp[p][0] + dp[p][1] - dp[p][2])) % mod
            dp[par][0] = (dp[par][0] * (2*dp[p][0] + 2*dp[p][1] - dp[p][2])) % mod
            dp[par][2] = (dp[par][2] * (dp[p][0] + dp[p][1] - dp[p][2])) % mod
    elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]]:
        Ind[p] += 1
    else:
        np = graph[p][Ind[p]]
        stack.append(np)
        Ind[p] += 1

print((dp[0][0] + dp[0][1] - dp[0][2])%mod)