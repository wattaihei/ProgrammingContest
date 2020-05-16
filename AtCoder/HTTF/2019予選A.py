N, M, L = map(int, input().split())
S = []
for _ in range(N):
    s = list(input())
    S.append(s)

boad = [['.' for _ in range(M)] for _ in range(M)]

# commandを受けて移動
def init_location(command):
    loc = [M//2, M//2]
    state = [0, 1]
    for s in command:
        if s == 'S':
            n_loc = [loc[0]+state[0], loc[1]+state[1]]
            if max(n_loc) != M-1 and min(n_loc) != 0:
                loc = n_loc
        elif s == 'L':
            if state == [0, 1]:
                state = [-1, 0]
            elif state == [-1, 0]:
                state = [0, -1]
            elif state == [0, -1]:
                state = [1, 0]
            else:
                state = [0, 1]
        else:
            if state == [0, 1]:
                state = [1, 0]
            elif state == [1, 0]:
                state = [0, -1]
            elif state == [0, -1]:
                state = [-1, 0]
            else:
                state = [0, 1]
    return loc


people = [[0 for _ in range(M)] for _ in range(M)]
for command in S:
    locx, locy = init_location(command)
    people[locx][locy] += 1

# blockに分けて整理してみる
block = [[0, 0], [0, 0]]
for i in range(M):
    for j in range(M):
        if i < M//2 and j <= M//2:
            block[0][0] += people[i][j]
        elif i >= M//2 and j < M//2:
            block[1][0] += people[i][j]
        elif i <= M//2 and j > M//2:
            block[0][1] += people[i][j]
        else:
            block[1][1] += people[i][j]



# なんか処理



# 壁
for i in range(M):
    boad[i][0] = '#'
    boad[i][M-1] = '#'
    boad[0][i] = '#'
    boad[M-1][i] = '#'

for i in range(M):
    print(''.join(boad[i]))