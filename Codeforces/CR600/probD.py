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

def main():
    N, M = map(int, input().split())
    uni = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        uni.Unite(a, b)

    R = {}
    for n in range(1, N+1):
        R[uni.Find_Root(n)] = n

    ans = 0
    root = uni.Find_Root(1)
    max_n = R[root]
    for n in range(1, N+1):
        rn = uni.Find_Root(n)
        if n > max_n:
            root = rn
            max_n = R[root]
        elif root != rn:
            ans += 1
            uni.Unite(root, rn)
            root = uni.Find_Root(root)
            max_n = max(max_n, R[rn])
        
    print(ans)

if __name__ == "__main__":
    main()