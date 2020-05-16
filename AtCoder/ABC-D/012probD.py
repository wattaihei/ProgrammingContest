import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    INF = 10**14
    D = [[INF for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        D[a-1][b-1] = t
        D[b-1][a-1] = t

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])

    for i in range(N):
        D[i][i] = 0

    ans = INF
    for i in range(N):
        d = max(D[i])
        ans = min(d, ans)
    print(ans)


if __name__ == "__main__":
    main()