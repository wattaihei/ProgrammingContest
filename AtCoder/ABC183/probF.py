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

def main():
    N, Q = map(int, input().rstrip().split())
    C = list(map(int, input().rstrip().split()))

    Query = [list(map(int, input().rstrip().split())) for _ in range(Q)]

    uni = UnionFind(N)
    Dic = [{C[i]-1 : 1} for i in range(N)]

    for q, x, y in Query:
        if q == 1:
            x -= 1; y -= 1
            rx = uni.Find_Root(x)
            ry = uni.Find_Root(y)
            if rx != ry:
                if len(Dic[rx]) < len(Dic[ry]):
                    rx, ry = ry, rx
                for k, c in Dic[ry].items():
                    if k in Dic[rx]:
                        Dic[rx][k] += c
                    else:
                        Dic[rx][k] = c
                uni.Unite(rx, ry)
                r = uni.Find_Root(rx)
                Dic[r] = Dic[rx]
        else:
            x -= 1; y -= 1
            r = uni.Find_Root(x)
            print(Dic[r][y] if y in Dic[r] else 0)


if __name__ == "__main__":
    main()