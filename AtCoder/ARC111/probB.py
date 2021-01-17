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

M = 4*10**5
N = int(input())
uni = UnionFind(M)
have_roop = [False]*M
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    a -= 1; b -= 1
    if uni.isSameGroup(a, b):
        have_roop[uni.Find_Root(a)] = True
    la = uni.Find_Root(a)
    lb = uni.Find_Root(b)
    uni.Unite(a, b)
    r = uni.Find_Root(b)
    have_roop[r] = have_roop[la] or have_roop[lb]

R = set()
for i in range(M):
    R.add(uni.Find_Root(i))

ans = 0
for r in R:
    ans += uni.Count(r)-1
    if have_roop[r]:
        ans += 1

print(ans)