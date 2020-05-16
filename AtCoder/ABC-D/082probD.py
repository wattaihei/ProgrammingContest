import sys
input = sys.stdin.readline

def main():
    S = list(input())
    X, Y = map(int, input().split())

    Xs = []
    Ys = []
    line = True
    first = True
    x0, y0 = 0, 0
    a = 0
    for s in S:
        if s == 'F':
            a += 1
        else:
            if first:
                if a > 0:
                    x0 = a
                a = 0
                first = False
                line = False
                continue
            if a > 0:
                if line:
                    Xs.append(a)
                else:
                    Ys.append(a)
                a = 0
            if line:
                line = False
            else:
                line = True
    if a > 0:
        if line:
            Xs.append(a)
        else:
            Ys.append(a)

    Lx = sum(Xs)+x0
    dpx = [[False for _ in range(2*Lx+1)] for _ in range(len(Xs)+1)]
    dpx[0][x0+Lx] = True

    for i, x in enumerate(Xs):
        for j in range(2*Lx+1):
            if j+x <= 2*Lx:
                dpx[i+1][j+x] = dpx[i][j] or dpx[i+1][j+x]
            if j-x >= 0:
                dpx[i+1][j-x] = dpx[i][j] or dpx[i+1][j-x]

    Ly = sum(Ys)+y0
    dpy = [[False for _ in range(2*Ly+1)] for _ in range(len(Ys)+1)]
    dpy[0][y0+Ly] = True

    for i, y in enumerate(Ys):
        for j in range(2*Ly+1):
            if j+y <= 2*Ly:
                dpy[i+1][j+y] = dpy[i][j] or dpy[i+1][j+y]
            if j-y >= 0:
                dpy[i+1][j-y] = dpy[i][j] or dpy[i+1][j-y]
    #print(Lx, Ly)
    if (not -Lx <= X <= Lx) or (not -Ly <= Y <= Ly): 
        print('No')
    elif dpx[-1][X+Lx] and dpy[-1][Y+Ly]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()