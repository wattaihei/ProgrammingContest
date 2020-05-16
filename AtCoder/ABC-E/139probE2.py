import sys
input = sys.stdin.readline


def main():
    N = int(input())
    graph = [[[] for _ in range(N)] for _ in range(N)]
    path = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        A = list(map(int, input().split()))
        for n in range(1, N-1):
            a, b = min(i, A[n]-1), max(i, A[n]-1)
            c, d = min(i, A[n-1]-1), max(i, A[n-1]-1)
            graph[c][d].append((a, b))
            path[a][b] += 1

    q = []
    for i in range(N-1):
        for j in range(i+1, N):
            if path[i][j] == 0:
                q.append((i, j))

    checked = [[False for _ in range(N)] for _ in range(N)]
    for i, j in q:
        checked[i][j] = True

    c = 0
    while q:
        c += 1
        qq = []
        for x, y in q:
            for nx, ny in graph[x][y]:
                path[nx][ny] -= 1
                if path[nx][ny] == 0:
                    checked[nx][ny] = True
                    qq.append((nx, ny))
        q = qq

    ok = True
    for i in range(N-1):
        for j in range(i+1, N):
            if not checked[i][j]:
                ok = False


    if not ok:
        print(-1)
    else:
        print(c)


if __name__ == "__main__":
    main()