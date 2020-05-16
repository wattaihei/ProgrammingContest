class UnionFind():
    # 作りたい要素数nで初期化
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズ
    def Count(self, x):
        return -self.root[self.Find_Root(x)]



import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
L = max(A).bit_length()

graph = [[] for _ in range(L)]
for i, a in enumerate(A):
    for k in range(L):
        if (1 << k) & a:
            graph[k].append(i)

UF = UnionFind(N)
for k in range(L):
    if not graph[k]: continue
    for p in graph[k]:
        UF.Unite(graph[k][0], p)

roots = set()
for i in range(N):
    roots.add(UF.Find_Root(i))


dis = [-1]*N
checked = [False]*N

def bfs(s):
    dis[s] = 0
    c = 0
    q = [s]
    ans = -1
    while q:
        c += 1
        qq = []
        for p in q:
            checked[p] = True
            print(p, checked, dis)
            for k in range(L):
                if (1 << k) & A[p]:
                    for np in graph[k]:
                        print(np)
                        if checked[np]: continue
                        if dis[np] == -1:
                            print(dis)
                            qq.append(np)
                            dis[np] = c
                        else:
                            ans = dis[np] + c
                            return ans
        q = qq
    return -1

def dfs(p, d):
    dis[p] = d
    for k in range(L):
        if (1 << k) & A[p]:
            for np in graph[k]:
                if dis[np] == -1:
                    dfs(np, d+1)

ans = N+1
for r in roots:
    a = bfs(r)
    if a != -1:
        ans = min(ans, a)
if ans == N+1:
    print(-1)
else:
    print(ans)