import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    graph = []
    for _ in range(M):
        a, b, d = map(int, input().split())
        graph.append([a-1, b-1, -d])

    INF = int(1E18)

    D = [INF for _ in range(N)]
    D[0] = 0

    for c in range(N-1):
        update = False
        for i, j, d in graph:
            if D[i] != INF and D[j] > D[i] + d:
                D[j] = D[i] + d
                update = True
        if not update:
            break

    negative = [False for _ in range(N)]
    for c in range(N):
        update = False
        for i, j, d in graph:
            if D[i] != INF and D[j] > D[i] + d:
                update = True
                D[j] = D[i] + d
                negative[j] = True
        if not update:
            break
    if negative[N-1]:
        print('inf')
    else:
        print(-D[N-1])

if __name__ == "__main__":
    main()