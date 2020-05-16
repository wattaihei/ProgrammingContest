N, M = map(int, input().split())
graph = [[] for _ in range(N)]
line = []
for _ in range(M):
    a, b = map(int, input().split())
    line.append([a-1, b-1])
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


ans = 0
for l in line:
    a, b = l
    qs = [a]
    checked = [False for _ in range(N)]
    checked[b] = True
    ok = False
    #print(a, b)
    first = True
    while qs:
        #print(qs)
        qqs = []
        for q in qs:
            checked[q] = True
            for k in graph[q]:
                #print(k)
                if k == b and first:
                    first = False
                elif k == b:
                    ok = True
                    break
                if not checked[k]:
                    qqs.append(k)
        qs = qqs
    if not ok:
        ans += 1

print(ans)