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

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
uni = UnionFind(N)
for _ in range(M):
    c, d = map(int, input().split())
    uni.Unite(c-1, d-1)

dic1 = {}
dic2 = {}
for n in range(N):
    r = uni.Find_Root(n)
    if not r in dic1:
        dic1[r] = A[n]
        dic2[r] = B[n]
    else:
        dic1[r] += A[n]
        dic2[r] += B[n]

ok = True
for k in dic1.keys():
    if dic1[k] != dic2[k]:
        ok = False
    
print("Yes" if ok else "No")