import sys
input = sys.stdin.readline

INF = 10**16

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

s = int(input())-1
K = int(input())
T = list(map(lambda x:int(x)-1, input().split())) + [s]

def bfs(start):
    q = [start]
    D = [-1]*N
    D[start] = 0
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = D[p] + 1
                    qq.append(np)
        q = qq
    
    ret = []
    for i, t in enumerate(T):
        ret.append(D[t])
    return ret

Distance = []
for t in T:
    Distance.append(bfs(t))


dp = [[INF]*(1<<(K+1)) for _ in range(K+1)] # 今iにいてbitだけ訪れた
dp[K][1<<K] = 0
for bit in range(1<<K, 1<<(K+1)):
    for i in range(K+1):
        if (1<<i)&bit:
            for ne in range(K+1):
                dp[ne][bit|(1<<ne)] = min(dp[ne][bit|(1<<ne)], dp[i][bit] + Distance[i][ne])

ans = INF
for k in range(K+1):
    ans = min(ans, dp[k][-1])
print(ans)