
qs = []
nm = []
Q = int(input())
for _ in range(Q):
    n, m = map(int, input().split())
    qs.append([[0 if a == '.' else 1 for a in list(input())] for _ in range(n)])
    nm.append([n, m])


for q in range(Q):
    state = qs[q]
    n, m = nm[q]
    rowm = []
    for k in range(n):
        rowm.append(sum(state[k]))
    
    colm = []
    for k in range(m):
        com = 0
        for i in range(n):
            com += state[i][k]
        colm.append(com)
    
    rowmax = max(rowm)
    colmax = max(colm)
    ans = n + m - rowmax - colmax
    rinds = [i for i, x in enumerate(rowm) if x == rowmax]
    cinds = [i for i, x in enumerate(colm) if x == colmax]
    cross = False
    for r in rinds:
        for c in cinds:
            if state[r][c] == 0:
                cross = True
                break
    if cross:
        ans -= 1
    print(ans)

