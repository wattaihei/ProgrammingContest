N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
C = list(map(int, input().split()))
C.sort(reverse=True)

q = [0]
checked = [False]*N
checked[0] = True
ans = 0
c = 0
score = [None for _ in range(N)]
score[0] = C[c]

while q:
    qq = []
    for p in q:
        for np in graph[p]:
            if not checked[np]:
                qq.append(np)
                checked[np] = True
                c += 1
                score[np] = C[c]
                ans += min(score[np], score[p])
    q = qq

print(ans)
for s in score:
    print(s, end=' ')
print()
