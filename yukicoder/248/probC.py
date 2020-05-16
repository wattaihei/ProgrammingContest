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

N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

uni = UnionFind(N)
Dic = {i:0 for i in range(N+1)}
for qnum, a, b in Query:
    if qnum == 1:
        #score = Dic[uni.Find_Root(a)] + Dic[uni.Find_Root(b)]
        uni.Unite(a, b)
        #Dic[uni.Find_Root(a)] = score
    elif qnum == 2:
        Dic[uni.Find_Root(a)] += b
    else:
        print(Dic[uni.Find_Root(a)])
