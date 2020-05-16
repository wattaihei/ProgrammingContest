import sys
input = sys.stdin.readline

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

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    union = UnionFind(N)
    checked = [False for _ in range(N)]
    for i in range(N):
        if checked[i]: continue
        checked[i] = True
        Con = [False]*N
        for j in graph[i]:
            Con[j] = True
        for k in range(N):
            if not Con[k]:
                union.Unite(i, k)
                checked[k] = True

    dic = {}
    for i in range(N):
        r = union.Find_Root(i)
        if not r in dic.keys():
            dic[r] = [i]
        else:
            dic[r].append(i)

    if len(dic) != 3:
        print(-1)
    else:
        E = M
        for v in dic.values():
            k = len(v)
            E += k*(k-1)//2
        if E != N*(N-1)//2:
            print(-1)
        else:
            ans = [None]*N
            for i, vs in enumerate(dic.values()):
                for v in vs:
                    ans[v] = i+1
            for a in ans:
                print(a, end=' ')
            print()

if __name__ == "__main__":
    main()