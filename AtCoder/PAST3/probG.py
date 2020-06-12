import sys
input = sys.stdin.readline

MAX = 500

N, X, Y = map(int, input().split())
Obj = [[False]*MAX for _ in range(MAX)]
for _ in range(N):
    x, y = map(int, input().split())
    Obj[x][y] = True

D = [[-1]*MAX for _ in range(MAX)]

def next(x, y):
    return [(x+1, y+1), (x, y+1), (x-1, y+1), (x+1, y), (x-1, y), (x, y-1)]

q = [(0, 0)]
D[0][0] = 0
while q and D[X][Y] == -1:
    qq = []
    for x, y in q:
        for nx, ny in next(x, y):
            if not Obj[nx][ny] and D[nx][ny] == -1 and -210 <= nx <= 210 and -210 <= ny <= 210:
                D[nx][ny] = D[x][y] + 1
                qq.append((nx, ny))
    q = qq


print(D[X][Y])