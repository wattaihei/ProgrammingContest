import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, w))
    graph[b-1].append((a-1, w))

def dfs(s):
    stack = [s]
    Color = [-1]*N
    Color[s] = 0
    while stack:
        p = stack.pop()
        for np, w in graph[p]:
            if Color[np] == -1:
                Color[np] = Color[p]^(w%2)
                stack.append(np)
    return Color

if __name__ == "__main__":
    Color = dfs(0)
    print(*Color, sep="\n")
