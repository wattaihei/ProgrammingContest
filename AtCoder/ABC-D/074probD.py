import heapq as hp
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    q = []
    for n in range(N):
        A = list(map(int, input().split()))
        for i, a in enumerate(A):
            if i > n:
                hp.heappush(q, (a, i, n))

    INF = int(1E17)
    D = [[INF for _ in range(N)] for _ in range(N)]
    using = []
    ok = True
    while q:
        d, a, b = hp.heappop(q)
        if D[a][b] < d:
            ok = False
            break
        elif D[a][b] > d:
            D[a][b] = d
            D[b][a] = d
            using.append((a, b))
            for n in range(N):
                if n == a or n == b:
                    continue
                if D[a][n] > D[b][n] + d:
                    D[a][n] = D[b][n] + d
                    D[n][a] = D[n][b] + d
                elif D[b][n] > D[a][n] + d:
                    D[b][n] = D[a][n] + d
                    D[n][b] = D[n][a] + d
    ans = 0
    for a, b in using:
        ans += D[a][b]
    if ok:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()