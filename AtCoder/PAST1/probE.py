import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

state = [[False]*(N+1) for _ in range(N+1)]

for query in Query:
    if query[0] == 1:
        a, b = query[1], query[2]
        state[a][b] = True
    elif query[0] == 2:
        a = query[1]
        for b in range(1, N+1):
            if state[b][a]:
                state[a][b] = True
    else:
        a = query[1]
        Xs = []
        for x in range(1, N+1):
            if state[a][x]:
                Xs.append(x)
        for x in Xs:
            for nx in range(1, N+1):
                if state[x][nx] and nx != a:
                    state[a][nx] = True

for n in range(1, N+1):
    print("".join(["Y" if state[n][m] else "N" for m in range(1, N+1)]))