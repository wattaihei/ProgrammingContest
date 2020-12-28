from bisect import bisect_left, bisect_right
class PersistentUnionFind():
    def __init__(self, n, INF=10**18):
        self.n = n
        self.par = [i for i in range(n)] # parent
        self.rnk = [0]*n # depth
        self.time = [INF]*n # when updated parent
        self.num1 = [[0] for _ in range(n)] # (time, count)
        self.num2 = [[1] for _ in range(n)]
        self.now = 0

    # root node when time is t
    def find(self, x, t):
        while t >= self.time[x]:
            x = self.par[x]
        return x

    # whether x, y is in same group
    def isSame(self, x, y, t):
        return self.find(x, t) == self.find(y, t)

    def unite(self, x, y):
        self.now += 1
        x = self.find(x, self.now)
        y = self.find(y, self.now)
        if (x == y): return

        if (self.rnk[x] < self.rnk[y]):
            x, y = y, x
        
        self.num1[x].append(self.now)
        self.num2[x].append(self.num2[x][-1] + self.num2[y][-1])

        self.par[y] = x
        self.time[y] = self.now
        if (self.rnk[x] == self.rnk[y]):
            self.rnk[x] += 1

    def size(self, x, t):
        x = self.find(x, t)
        ind = bisect_right(self.num1[x], t) - 1
        return self.num2[x][ind]


if __name__ == "__main__":
    
    import sys
    input = sys.stdin.buffer.readline

    N, M = map(int, input().rstrip().split())

    uni = PersistentUnionFind(N)
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        uni.unite(a-1, b-1)

    Q = int(input())
    for _ in range(Q):
        x, y, z = map(int, input().rstrip().split())
        x -= 1; y -= 1
        ng = 0; ok = M
        while ok-ng > 1:
            t = (ok+ng)//2
            if uni.isSame(x, y, t):
                s = uni.size(x, t)
            else:
                s = uni.size(x, t) + uni.size(y, t)
            if s >= z:
                ok = t
            else:
                ng = t
        print(ok)