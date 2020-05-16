import sys
input = sys.stdin.readline


N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

if K > N:
    print(-1)
else:
    D = [-1]*N
    D[0] = 0
    q = [0]
    while q:
        qq = []
        for p in q:
            for np in graph[p]:
                if D[np] == -1:
                    D[np] = D[p] + 1
                    qq.append(np)
        q = qq
    
    D.sort()
    print(sum(D[:K]))