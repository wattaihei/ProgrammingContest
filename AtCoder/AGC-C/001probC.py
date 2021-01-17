import sys
input = sys.stdin.buffer.readline

INF = 10**18

N, K = map(int, input().rstrip().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = INF
if K%2 == 0:
    d = K//2
    for c in range(N):
        q = [c]
        checked = [False]*N
        checked[c] = True
        for _ in range(d):
            qq = []
            for p in q:
                for np in graph[p]:
                    if not checked[np]:
                        checked[np] = True
                        qq.append(np)
            q = qq
        
        cnt = 0
        for i in range(N):
            if not checked[i]: cnt += 1
        ans = min(ans, cnt)
else:
    d = K//2
    for i in range(N):
        for j in graph[i]:
            if i > j:
                q = [i, j]
                checked = [False]*N
                checked[i] = True
                checked[j] = True
                for _ in range(d):
                    qq = []
                    for p in q:
                        for np in graph[p]:
                            if not checked[np]:
                                checked[np] = True
                                qq.append(np)
                    q = qq
                
                cnt = 0
                for p in range(N):
                    if not checked[p]: cnt += 1
                ans = min(ans, cnt)

print(ans)