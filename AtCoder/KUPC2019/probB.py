import sys
input = sys.stdin.readline

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



N, M, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
AB = [list(map(int, input().split())) for _ in range(M)]

union = UnionFind(N-1)
for a, b in AB:
    union.Unite(a-1, b-1)

dic = {}
for n in range(N):
    r = union.Find_Root(n)
    if not r in dic.keys():
        dic[r] = [n]
    else:
        dic[r].append(n)

L = len(dic)

dp = [[0 for _ in range(W+1)] for _ in range(L+1)]

for i, A in enumerate(dic.values()):
    pw, pv = 0, 0
    for a in A:
        pw += WV[a][0]
        pv += WV[a][1]

    for w in range(W+1):
        if w-pw < 0:
            dp[i+1][w] = dp[i][w]
        else:
            dp[i+1][w] = max(dp[i][w], dp[i][w-pw]+pv)

print(dp[L][W])