N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

C = list(map(int, input().split()))
Clist = [False for _ in range(N)]
for c in C:
    Clist[c-1] = True

ng = [[] for _ in range(N)]
checked = [False for _ in range(N)]
qs = [C[0]]
root = [C[0] for _ in range(N)] 
while qs:
    qqs = []
    
    for q in qs:
        if Clist[q]:
            root[q] = q
        checked[q] = True
        for a in graph[q]:
            root[a] = root[q]
            if not checked[a]:
                qqs.append(a)
                if Clist[a]:
                    ng[root[a]].append(a)
                    ng[a].append(root[a])
    qs = qqs
print(ng)

ans = 'Yes'
for n in ng:
    if len(n) > 2:
        ans = 'trumpet'

print(ans)