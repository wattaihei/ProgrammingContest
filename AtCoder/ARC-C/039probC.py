import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

offset = 5*10**8

def sg(a, b):
    return (a+offset)*10**9 + (b+offset)

def db(ab):
    return ab//(10**9)-offset, ab%(10**9)-offset

L = {sg(1, 0): sg(-1, 0)}
R = {sg(-1, 0): sg(1, 0)}
U = {sg(0, -1): sg(0, 1)}
D = {sg(0, 1): sg(0, -1)}

x, y = 0, 0
for s in S:
    xy = sg(x, y)
    if s == "L":
        if not xy in L.keys():
            nx, ny = x-1, y
        else:
            nx, ny = db(L[xy])
    elif s == "R":
        if not xy in R.keys():
            nx, ny = x+1, y
        else:
            nx, ny = db(R[xy])
    elif s == "U":
        if not xy in U.keys():
            nx, ny = x, y+1
        else:
            nx, ny = db(U[xy])
    elif s == "D":
        if not xy in D.keys():
            nx, ny = x, y-1
        else:
            nx, ny = db(D[xy])
    
    nxy = sg(nx, ny)
    if not nxy in L.keys():
        lxy = sg(nx-1, ny)
    else:
        lxy = L[nxy]
    if not nxy in R.keys():
        rxy = sg(nx+1, ny)
    else:
        rxy = R[nxy]
    if not nxy in U.keys():
        uxy = sg(nx, ny+1)
    else:
        uxy = U[nxy]
    if not nxy in D.keys():
        dxy = sg(nx, ny-1)
    else:
        dxy = D[nxy]
    
    L[rxy] = lxy
    R[lxy] = rxy
    U[dxy] = uxy
    D[uxy] = dxy

    x, y = nx, ny


print(x, y)