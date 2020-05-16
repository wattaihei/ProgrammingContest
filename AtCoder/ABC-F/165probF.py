import sys
input = sys.stdin.readline
from bisect import bisect_left

INF = 10**17

N = int(input())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


stack = [0]
ans = [-1]*N
dp = [INF]*(N+1)
to_rev = [(-1, -1) for _ in range(N)]
while stack:
    p = stack.pop()
    if p >= 0:
        ind = bisect_left(dp, A[p])
        to_rev[p] = (ind, dp[ind])
        dp[ind] = A[p]
        ans[p] = bisect_left(dp, INF)
        stack.append(~p)
        for np in graph[p]:
            if ans[np] == -1:
                stack.append(np)
    else:
        p = ~p
        ind, score = to_rev[p]
        dp[ind] = score

print(*ans, sep="\n")