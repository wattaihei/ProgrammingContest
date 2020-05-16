import sys
input = sys.stdin.readline


N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


Par = [-1]*N
que = []

childs = [0]*N
stack = [0]
Ind = [0]*N
D = [0]*N
while stack:
    p = stack[-1]
    if Ind[p] == len(graph[p]):
        stack.pop()
        if stack:
            par = stack[-1]
            Par[p] = par
            childs[par] += childs[p] + 1
    elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]]:
        Ind[p] += 1
    else:
        np = graph[p][Ind[p]]
        D[np] = D[p] + 1
        Ind[p] += 1
        stack.append(np)


B = []
for n in range(N):
    B.append(D[n]-childs[n])

B.sort(reverse=True)
print(sum(B[:K]))