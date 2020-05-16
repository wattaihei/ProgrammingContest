N = int(input())
a, b = map(int, input().split())
M = int(input())
mod = int(1E9+7)

graph = [[] for _ in range(N)]
for _ in range(M):
    c, d = map(int, input().split())
    graph[c-1].append(d-1)
    graph[d-1].append(c-1)

dp = [0 for _ in range(N)] # 頂点iまで最短でいったときの経路数

checked = [False for _ in range(N)]
qs = set([a-1])
dp[a-1] = 1
stop = False
while True:
    #print(qs)
    #print(dp)
    qqs = set()
    for q in qs:
        checked[q] = True
    for q in qs:
        for p in graph[q]:
            if checked[p]:
                continue
            dp[p] = (dp[p] + dp[q]) % mod
            qqs.add(p)
            if p == b-1:
                stop = True
    if stop:
        break
    qs = qqs

print(dp[b-1]%mod)