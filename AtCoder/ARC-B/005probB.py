
N = 9
sx, sy, d = map(str, input().split())
x, y = int(sx)-1, int(sy)-1
state = [[int(a) for a in list(input())] for _ in range(N)]

ans = [state[y][x]]
for _ in range(3):
    if d == 'R':
        if x == N-1:
            x -= 1
            d = 'L'
        else:
            x += 1
    elif d == 'L':
        if x == 0:
            x += 1
            d = 'R'
        else:
            x -= 1
    elif d == 'U':
        if y == 0:
            y += 1
            d = 'D'
        else:
            y -= 1
    elif d == 'D':
        if y == N-1:
            y -= 1
            d = 'U'
        else:
            y += 1
    elif d == 'RU':
        if x == N-1 and y == 0:
            d = 'LD'
            x -= 1
            y += 1
        elif x == N-1:
            d = 'LU'
            x -= 1
            y -= 1
        elif y == 0:
            d = 'RD'
            x += 1
            y += 1
        else:
            x += 1
            y -= 1
    elif d == 'RD':
        if x == N-1 and y == N-1:
            d = 'LU'
            x -= 1
            y -= 1
        elif x == N-1:
            d = 'LD'
            x -= 1
            y += 1
        elif y == N-1:
            d = 'RU'
            x += 1
            y -= 1
        else:
            x += 1
            y += 1
    elif d == 'LU':
        if x == 0 and y == 0:
            d = 'RD'
            x += 1
            y += 1
        elif x == 0:
            d = 'RU'
            x += 1
            y -= 1
        elif y == 0:
            d = 'LD'
            x -= 1
            y += 1
        else:
            x -= 1
            y -= 1
    elif d == 'LD':
        if x == 0 and y == N-1:
            d = 'RU'
            x += 1
            y -= 1
        elif x == 0:
            d = 'RD'
            x += 1
            y += 1
        elif y == N-1:
            d = 'LU'
            x -= 1
            y -= 1
        else:
            x -= 1
            y += 1

    ans.append(state[y][x])

print(''.join([str(a) for a in ans]))