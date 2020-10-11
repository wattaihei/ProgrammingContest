import sys
input = sys.stdin.buffer.readline



def solve(N, graph):
    stack = [0]
    Par = [-1]*N
    checked = [False]*N
    Children = [1]*N
    checked[0] = True
    Ch = [-1]*N
    while stack:
        p = stack.pop()
        if p >= 0:
            stack.append(~p)
            for np in graph[p]:
                if not checked[np]:
                    checked[np] = True
                    Par[np] = p
                    Ch[p] = np
                    stack.append(np)
        else:
            p = ~p
            if p > 0:
                Children[Par[p]] += Children[p]
    
    if N%2 == 1:
        return 1, graph[0][0]+1, 1, graph[0][0]+1
    for n in range(N):
        if Children[n] == N//2:
            m = Par[n]
            l = n
            while Ch[l] != -1:
                l = Ch[l]
            return Par[l]+1, l+1, m+1, l+1
            
    return 1, graph[0][0]+1, 1, graph[0][0]+1

Q = int(input())
for _ in range(Q):
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    a, b, c, d = solve(N, graph)
    print(a, b)
    print(c, d)