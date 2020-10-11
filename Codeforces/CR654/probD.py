import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, K in Query:
    state = [[0]*N for _ in range(N)]
    if K%N == 0:
        print(0)
        h1 = K//N
        for i in range(h1):
            for r in range(N):
                state[r][(r+i)%N] = 1
        for i in range(h1, N):
            for r in range(N):
                state[r][(r+i)%N] = 0
    else:
        print(2)
        h1 = K//N
        am = K%N
        for k in range(N):
            state[k][k] = 1 if k < am else 0
        for i in range(1, h1+1):
            for r in range(N):
                state[r][(r+i)%N] = 1
        for i in range(h1+1, N):
            for r in range(N):
                state[r][(r+i)%N] = 0
    
    for s in state:
        print(*s, sep="")