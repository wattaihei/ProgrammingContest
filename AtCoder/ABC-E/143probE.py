import sys
input = sys.stdin.readline


def main():
    N, M, L = map(int, input().split())
    INF = 10**13
    dis = [[INF for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        dis[a-1][b-1] = c
        dis[b-1][a-1] = c
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
    
    movable = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and dis[i][j] <= L:
                movable[i].append(j)
    

    for s, t in Query:
        s, t = s-1, t-1
        q = movable[s]
        checked = [False]*N
        ok = False
        for p in q:
            if p == t:
                ok = True
                break
            checked[p] = True
        checked[s] = True
        
        if ok:
            print(0)
            continue
        c = 0
        while q:
            c += 1
            qq = []
            for p in q:
                for np in movable[p]:
                    if np == t:
                        ok = True
                        break
                    if not checked[np]:
                        qq.append(np)
                        checked[np] = True
            if ok: break
            q = qq
        if ok:
            print(c)
        else:
            print(-1)



            



if __name__ == "__main__":
    main()