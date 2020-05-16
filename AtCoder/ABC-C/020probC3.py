import heapq as hp

H, W, T = map(int, input().split())
state = []
for h in range(H):
    S = list(input())
    s_list = []
    for w in range(W):
        if S[w] == 'S':
            s = (h, w)
        if S[w] == 'G':
            g = (h, w)
        if S[w] == '#':
            s_list.append(1)
        else:
            s_list.append(0)
    state.append(s_list)

l = 0
r = T
t = (l+r)//2
while True:
    # AOJ GRL_1_A Single Sourse Shortest Path
    graph = [[[] for _ in range(W)] for _ in range(H)]
    INF = 0
    for h in range(H):
        for w in range(W):
            if h != 0:
                d = t if state[h-1][w] == 1 else 1
                graph[h][w].append((d, h-1, w))
            if h != H-1:
                d = t if state[h+1][w] == 1 else 1
                graph[h][w].append((d, h+1, w))
            if w != 0:
                d = t if state[h][w-1] == 1 else 1
                graph[h][w].append((d, h, w-1))
            if w != W-1:
                d = t if state[h][w+1] == 1 else 1
                graph[h][w].append((d, h, w+1)) 
    
    INF = T*H*W
    D = [[INF for _ in range(W)] for _ in range(H)] # 頂点iへの最短距離がD[i]
    D[s[0]][s[1]] = 0
    q = [] # しまっていく優先度付きキュー
    hp.heappush(q, (0, s[0], s[1]))

    while q:
        nd, nh, nw = hp.heappop(q) # 一番距離が近いものを取ってくる
        if D[nh][nw] < nd: # 追加した後の残骸は見ない
            continue
        for d, h, w in graph[nh][nw]:
            if D[h][w] > D[nh][nw] + d: # 隣接するやつの中で今よりも近くなれるなら更新
                D[h][w] = D[nh][nw] + d
                hp.heappush(q, (D[h][w], h, w))

    Dg = D[g[0]][g[1]]
    #print(t, Dg, l, r)
    if Dg > T:
        r = t
    else:
        l = t
    if l+1 == r or l==r:
        break
    t = (l+r)//2
print(l)