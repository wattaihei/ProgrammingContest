R, C = map(int, input().split())
state = [list(input()) for _ in range(R)]

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

union = UnionFind(10000)

ans = 0
for r in range(R):
    for c in range(C):
        if state[r][c] == '*':
            continue
        next = []
        if r != 0:  next.append((r-1, c))
        if r != R-1:  next.append((r+1, c))
        if c != 0:  next.append((r, c-1))
        if c != C-1:  next.append((r, c+1))
        for nr, nc in next:
            if state[nr][nc] == '.':
                union.Unite(100*nr+nc, 100*r+c)


Root = set()
for r in range(R):
    for c in range(C):
        if state[r][c] == '*':
            continue
        l = union.Find_Root(100*r+c)
        rr, rc = l//100, l%100
        Root.add((rr, rc))

checked = [[False for _ in range(C)] for _ in range(R)]
for rr, rc in Root:
    q = [(rr, rc)]
    checked[rr][rc] = True
    count = 0
    score = [0, 0]
    while q:
        score[count%2] += len(q)
        qq = []
        for r, c in q:
            next = []
            if r != 0:  next.append((r-1, c))
            if r != R-1:  next.append((r+1, c))
            if c != 0:  next.append((r, c-1))
            if c != C-1:  next.append((r, c+1))
            for nr, nc in next:
                if state[nr][nc] == '*':
                    continue
                if not checked[nr][nc]:
                    qq.append((nr, nc))
                    checked[nr][nc] = True
        q = qq
        count += 1
    ans += max(score)

print(ans)