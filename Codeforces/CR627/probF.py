import sys
input = sys.stdin.readline
INF = 10**18

N = int(input())
Color = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

Score = [{} for _ in range(N)]
Max = [-INF]*N
for i, c in enumerate(Color):
    Max[i] = 1 if c else -1

def dfs(s):
    stack = [s]
    Ind = [0]*N
    while stack:
        p = stack[-1]
        if Ind[p] == len(graph[p]):
            # ret
            stack.pop()
            if stack:
                par = stack[-1]
                Max[par] += max(Max[p], 0)
        elif len(stack) > 1 and graph[p][Ind[p]] == stack[-2]:
            Ind[p] += 1
        else:
            stack.append(graph[p][Ind[p]])
            Ind[p] += 1

ans = [-INF]*N
def dfs2(s):
    ans[s] = Max[s]
    stack = [s]
    Ind = [0]*N
    while stack:
        p = stack[-1]
        if Ind[p] == len(graph[p]):
            # ret
            stack.pop()
        elif len(stack) > 1 and graph[p][Ind[p]] == stack[-2]:
            Ind[p] += 1
        else:
            ch = graph[p][Ind[p]]
            ans[ch] = max((ans[p] - max(Max[ch], 0)), 0) + Max[ch]
            stack.append(ch)
            Ind[p] += 1

dfs(0)
#print(Max)
dfs2(0)
print(*ans)