import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N-1辺表示をグラフ表示に
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
S, T = map(lambda x:int(x)-1, input().split())


q = {S}
checked = [False]*N
checked[S] = True

ok = False
c = 0
while q:
    c += 1
    qq = set()
    if c % 3 == 0:
        for p in q:
            for np in graph[p]:
                if np == T:
                    ok = True
                    break
                if not checked[np]:
                    qq.add(np)
                    checked[np] = True
    else:
        for p in q:
            for np in graph[p]:
                qq.add(np)
    if ok:
        break
    q = qq

if ok:
    print(c//3)
else:
    print(-1)