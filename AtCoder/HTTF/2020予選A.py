import random

N, M, B = map(int, input().split())
gy, gx = map(int, input().split())
Robots = [list(map(str, input().split())) for _ in range(M)]
Block = [list(map(int, input().split())) for _ in range(B)]

block_state = [[False for _ in range(N)] for _ in range(N)]
for i, j in Block:
    block_state[i][j] = True

state = [[None for _ in range(N)] for _ in range(N)]

def up_limit(i, j):
    init_i = i
    loop = False
    while not block_state[i-1][j]:
        i -= 1
        if i==-1: i += N
        if i == init_i:
            loop = True
            break
    if loop:
        return False
    else:
        return i


def down_limit(i, j):
    if i == N-1: i -= N
    init_i = i
    loop = False
    while not block_state[i+1][j]:
        i += 1
        if i==N-1: i -= N
        if i == init_i:
            loop = True
            break
    if loop:
        return False
    elif i == N-1:
        return N-1
    else:
        return i

def left_limit(i, j):
    init_j = j
    loop = False
    while not block_state[i][j-1]:
        j -= 1
        if j==-1: j += N
        if j == init_j:
            loop = True
            break
    if loop:
        return False
    else:
        return j

def right_limit(i, j):
    if j == N-1: j -= N
    init_j = j
    loop = False
    while not block_state[i][j+1]:
        j += 1
        if j==N-1: j -= N
        if j == init_j:
            loop = True
            break
    if loop:
        return False
    elif j == -1:
        return N-1
    else:
        return j

q = [(gy, gx)]
for _ in range(4):
    qq = []
    for py, px in q:
        u = up_limit(py, px)
        d = down_limit(py, px)
        r = right_limit(py, px)
        l = left_limit(py, px)
        if u is False:
            continue
        if u != py and state[u][px] is None:
            state[u][px] = 'D'
            qq.append((u, px))
        if d != py and state[d][px] is None:
            state[d][px] = 'U'
            qq.append((d, px))
        if r is False:
            continue
        if r != px and state[py][r] is None:
            state[py][r] = 'L'
            qq.append((py, r))
        if l != px and state[py][l] is None:
            state[py][l] = 'R'
            qq.append((py, l))
    q = qq

"""
for sy, sx, di in Robots:
    y, x = int(sy), int(sx)
    if di == 'U':
        u = up_limit(y, x)
        if not u is False:
            ny = y
            while True:
                if not state[ny][x] is None:
                    break
                if block_state[ny][x]:
"""                    
ans = []
for i in range(N):
    for j in range(N):
        if not state[i][j] is None:
            ans.append((i, j, state[i][j]))
print(len(ans))
for y, x, c in ans:
    print(y, x, c)