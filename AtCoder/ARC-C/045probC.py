import sys
input = sys.stdin.readline

N, X = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

S = [-1]*N
S[0] = 0
q = [0]
while q:
    qq = []
    for p in q:
        s = S[p]
        for np, c in graph[p]:
            if S[np] == -1:
                S[np] = s^c
                qq.append(np)
    q = qq

dic = {}
for s in S:
    if not s in dic.keys():
        dic[s] = 1
    else:
        dic[s] += 1

    
ans = 0
if X == 0:
    for v in dic.values():
        ans += v*(v-1)//2
else:
    for s, c in dic.items():
        ns = s^X
        if ns in dic.keys():
            ans += c*dic[ns]
    ans //= 2

print(ans)