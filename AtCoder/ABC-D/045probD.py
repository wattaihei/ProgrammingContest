H, W, N = map(int, input().split())


graph = {}
for _ in range(N):
    a, b = list(map(int, input().split()))
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            na, nb = a-1+i, b-1+j
            if 1 <= na <= H-2 and 1 <= nb <= W-2:
                if not na in graph.keys():
                    graph[na] = {nb: 1}
                elif not nb in graph[na].keys():
                    graph[na][nb] = 1
                else:
                    graph[na][nb] += 1
#print(graph)
ans = [0 for _ in range(10)]
S = 0
for a, v_graph in graph.items():
    for b, v in v_graph.items():
        ans[v] += 1
        S += 1
ans[0] = (H-2)*(W-2) - S
for a in ans:
    print(a)