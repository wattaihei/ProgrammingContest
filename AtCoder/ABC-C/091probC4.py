N = int(input())
V = 2*N
Red = [list(map(int, input().split())) for _ in range(N)]
Blue = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(V)]
for i in range(N):
    for j in range(N):
        a, b = Red[i]
        c, d = Blue[j]
        if a < c and b < d:
            j += N
            graph[i].append(j)
            graph[j].append(i)

match = [-1]*V # マッチングペア
used = [False]*V # DFSですでに調べたか

# search increasing path
def dfs(v):
    used[v] = True
    for nv in graph[v]:
        w = match[nv]
        if w < 0 or (not used[w] and dfs(w)):
            match[v] = nv
            match[nv] = v
            return True
    return False


def bipartite_matching():
    res = 0
    global match
    match = [-1]*V
    for v in range(V):
        if match[v] < 0:
            global used
            used = [0]*V
            if dfs(v):
                res += 1
    return res


if __name__ == '__main__':
    print(bipartite_matching())