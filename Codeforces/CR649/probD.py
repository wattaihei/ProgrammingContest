import sys
input = sys.stdin.buffer.readline

INF = 10**18

N, M, K = map(int, input().split())
graph = [[] for _ in range(K)]
for _ in range(M):
    a, b = map(int, input().split())
    if a <= K and b <= K:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

ans = []
D = [-1]*K
Par = [-1]*K
iscycle = INF
stop = INF
for s in range(K):
    if D[s] != -1: continue
    D[s] = 0
    stack = [s]
    dp = [[s], []]
    while stack and iscycle == INF:
        p = stack.pop()
        for np in graph[p]:
            if D[np] == -1:
                Par[np] = p
                D[np] = D[p] + 1
                stack.append(np)
                dp[D[np]%2].append(np)
            elif (D[p] - D[np] + 1) % 2 != 0:
                stop = Par[np]
                Par[np] = p
                iscycle = np
                break
    if iscycle != INF:
        break
    if len(dp[0]) > len(dp[1]):
        for p in dp[0]:
            ans.append(p+1)
    else:
        for p in dp[1]:
            ans.append(p+1)


if iscycle == INF:
    ans = ans[:(K+1)//2]
    print(1)
    print(*ans)
else:
    ans = [stop+1]
    s = iscycle
    while s != stop:
        ans.append(s+1)
        s = Par[s]
    print(2)
    print(len(ans))
    print(*ans)