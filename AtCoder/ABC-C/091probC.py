N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]

state = [[0 for _ in range(N)] for _ in range(N)]
for i, (a, b) in enumerate(ab):
    for j, (c, d) in enumerate(cd):
        if a < c and b < d:
            state[i][j] = 1
for s in state:
    print(s)
