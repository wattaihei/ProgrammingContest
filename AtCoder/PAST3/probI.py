import sys
input = sys.stdin.readline

N = int(input())
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

state = [[i for i in range(N)] for _ in range(2)]

isInverse = 0
for query in Query:
    if query[0] == 1:
        a, b = query[1]-1, query[2]-1
        state[isInverse][a], state[isInverse][b] = state[isInverse][b], state[isInverse][a]
    elif query[0] == 2:
        a,b = query[1]-1, query[2]-1
        state[isInverse^1][a], state[isInverse^1][b] = state[isInverse^1][b], state[isInverse^1][a]
    elif query[0] == 3:
        isInverse ^= 1
    else:
        a, b = query[1]-1, query[2]-1
        if isInverse:
            row = state[0][b]
            col = state[1][a]
        else:
            row = state[0][a]
            col = state[1][b]
        print(row*N+col)