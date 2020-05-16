class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return 
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

N = int(input())
S1 = list(input())
S2 = list(input())

Alp = [chr(i) for i in range(65, 65+26)]
UF = UnionFind(26)

decided = {}
for s1, s2 in zip(S1, S2):
    if s1 in Alp and s2 in Alp:
        i1 = Alp.index(s1)
        i2 = Alp.index(s2)
        UF.Unite(i1, i2)
    elif s1 in Alp:
        decided[s1] = s2
    elif s2 in Alp:
        decided[s2] = s1

for i in range(26):
    a = Alp[i]
    for j in range(26):
        b = Alp[j]
        if UF.isSameGroup(i, j) and b in decided.keys():
            decided[a] = decided[b]

ans = 1
for n, (s1, s2) in enumerate(zip(S1, S2)):
    if s1 in Alp and s2 in Alp:
        if not s1 in decided.keys():
            if n != 0:
                ans *= 10
            else:
                ans *= 9
            i = Alp.index(s1)
            for j in range(26):
                if UF.isSameGroup(i, j):
                    decided[Alp[j]] = '-1'
print(ans)