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
input = sys.stdin.buffer.readline
N, K = map(int, input().rstrip().split())
state = [list(map(int, input().rstrip().split())) for _ in range(N)]

mod = 998244353

NN = 1000 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

uni = UnionFind(N)

ans = 1

for h1 in range(N):
    for h2 in range(h1+1, N):
        ok = True
        for w in range(N):
            if state[h1][w] + state[h2][w] > K:
                ok = False
                break
        if ok:
            uni.Unite(h1, h2)

dic1 = {}
for h in range(N):
    r = uni.Find_Root(h)
    if not r in dic1:
        dic1[r] = uni.Count(r)

for a in dic1.values():
    ans = ans * g1[a] % mod


uni2 = UnionFind(N)
for h1 in range(N):
    for h2 in range(h1+1, N):
        ok = True
        for w in range(N):
            if state[w][h1] + state[w][h2] > K:
                ok = False
                break
        if ok:
            uni2.Unite(h1, h2)

dic2 = {}
for h in range(N):
    r = uni2.Find_Root(h)
    if not r in dic2:
        dic2[r] = uni2.Count(r)

for a in dic2.values():
    ans = ans * g1[a] % mod

print(ans)