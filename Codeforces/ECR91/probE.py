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
T = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(M-1)]

uni = UnionFind(M)
dic = {}
for i, t in enumerate(T):
    if t in dic:
        dic[t].add(i)
    else:
        dic[t] = {i}

uniToKey = [i for i in range(M+1)]
ans = N-1
for L in dic.values():
    for node in L:
        if node - 1 in L:
            ans -= 1

print(ans)

for a, b in Query:
    a = uni.Find_Root(a)
    b = uni.Find_Root(b)
    ka = uniToKey[a]
    kb = uniToKey[b]
    if len(dic[ka]) < len(dic[kb]):
        newkey = kb
        for node in dic[ka]:
            if node - 1 in dic[kb]:
                ans -= 1
            if node + 1 in dic[kb]:
                ans -= 1
        for node in dic[ka]:
            dic[kb].add(node)
    else:
        newkey = ka
        for node in dic[kb]:
            if node - 1 in dic[ka]:
                ans -= 1
            if node + 1 in dic[ka]:
                ans -= 1
        for node in dic[kb]:
            dic[ka].add(node)
    uni.Unite(a, b)
    r = uni.Find_Root(a)
    uniToKey[r] = newkey
    print(ans)
