import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

D = [-1]*N
D[0] = 0
Childs = [1]*N
ans = [-1]*N

stack = [0]
while stack:
    p = stack.pop()
    if p >= 0:
        stack.append(~p)
        for np in graph[p]:
            if D[np] == -1:
                D[np] = D[p] + 1
                stack.append(np)
    else:
        p = ~p
        t1 = 0
        t2 = 0
        for np in graph[p]:
            if D[np] > D[p]:
                t1 += Childs[np]
                t2 += Childs[np]**2
                Childs[p] += Childs[np]
        ans[p] = (t1**2 - t2) + 2*t1 + 1


print(*ans, sep="\n")