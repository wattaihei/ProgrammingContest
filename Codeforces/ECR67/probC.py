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

N, M = map(int, input().split())
TLR = [list(map(int, input().split())) for _ in range(M)]

uni = UnionFind(N)
for T, L, R in TLR:
    if T == 1:
        for n in range(L, R+1):
            uni.Unite(L, n)

ok = True
for T, L, R in TLR:
    if T == 0:
        if uni.isSameGroup(L, R):
            ok = False

if not ok:
    print('NO')
else:
    print('YES')
    ans = [10**6]
    for i in range(1, N):
        if uni.isSameGroup(i, i+1):
            ans.append(ans[-1]+1)
        else:
            ans.append(ans[-1]-1)
    for a in ans:
        print(a, end=' ')
    print()