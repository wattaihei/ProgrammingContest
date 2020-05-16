# AOJ GRL_7_A "Bipartite Matching"
# 頂点数V1とV2の隣接リストから最大二部マッチング

V1, V2, E = map(int, input().split())
V = V1 + V2
graph = [[] for _ in range(V)]
for _ in range(E):
    a, b = map(int, input().split())
    b += V1
    graph[a].append(b)
    graph[b].append(a)

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