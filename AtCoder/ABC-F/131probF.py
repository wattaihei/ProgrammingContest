import sys
input = sys.stdin.readline


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    MAX = 10**5
    Xs = [[] for _ in range(MAX+1)]
    Ys = [[] for _ in range(MAX+1)]
    for i, (x, y) in enumerate(XY):
        Xs[x].append(i)
        Ys[y].append(i)

    ans = 0
    checked = [False]*N
    for i in range(N):
        if checked[i]: continue
        q = [i]
        checked[i] = True
        X = set()
        Y = set()
        c = 0
        while q:
            qq = []
            for p in q:
                x, y = XY[p]
                X.add(x)
                Y.add(y)
                c += 1
                for ni in Xs[x]:
                    if not checked[ni]:
                        checked[ni] = True
                        qq.append(ni)
                for ni in Ys[y]:
                    if not checked[ni]:
                        checked[ni] = True
                        qq.append(ni)
            q = qq
        ans += len(X)*len(Y)-c

    print(ans)


if __name__ == "__main__":
    main()