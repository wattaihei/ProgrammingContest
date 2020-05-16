class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
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

    def Count(self, x):
        return -self.root[self.Find_Root(x)]
    

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(K)]


uni = UnionFind(N+1)
for x, y in XY:
    uni.Unite(x, y)

ans = K
roots = set()
for n in range(1, N+1):
    r = uni.Find_Root(n)
    if not r in roots:
        roots.add(r)
        ans -= uni.Count(r) - 1
print(ans)
