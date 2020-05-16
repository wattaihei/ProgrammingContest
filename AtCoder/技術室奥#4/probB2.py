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

checked = [False for _ in range(N)]

q = C[0]
def color(q):
    checked[q] = True
    if :
        return 
    bra = 0
    leaf = True
    for p in graph[q]:
        if not checked[p]:
            leaf = False
            bra += color(p)
    if leaf:
        
    return bra