N, K = map(int, input().split()) # 横に2個

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

#print(graph)

dis = [[] for _ in range(N)]
for i in range(N):
    d = 0
    checked = [False for _ in range(N)]
    checked[i] = True
    qs = [i]
    #print(i)
    while qs:
        qqs = []
        for p in qs:
            for k in graph[p]:
                if not checked[k]:
                    checked[k] = True
                    qqs.append(k)
        d += 1
        if d > K and qqs:
            #print(d, qqs)
            for l in qqs:
                dis[i].append(l)
        qs = qqs

ans = 0
while True:
    end = True
    max = 0
    for i, d in enumerate(dis):
        if len(d) > 0:
            end = False
        if len(d) > max:
            rem = i
            max = len(d)
    if end:
        break
    for p in dis[rem]:
        dis[p].remove(rem)
    dis[rem] = []
    #print(rem)
    ans += 1
    #print(dis)
print(ans)