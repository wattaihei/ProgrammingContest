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


N, K, L = map(int, input().split())
U1 = UnionFind(N)
U2 = UnionFind(N)
for _ in range(K):
    a, b = map(int, input().split())
    U1.Unite(a, b)
for _ in range(L):
    a, b = map(int, input().split())
    U2.Unite(a, b)

Roots = [0]
dic = {}
for n in range(1, N+1):
    r1 = U1.Find_Root(n)
    r2 = U2.Find_Root(n)
    r = r1*2*N + r2
    Roots.append(r)
    if not r in dic.keys():
        dic[r] = 1
    else:
        dic[r] += 1
    
ans = []
for n in range(1, N+1):
    ans.append(dic[Roots[n]])

print(" ".join([str(a) for a in ans]))