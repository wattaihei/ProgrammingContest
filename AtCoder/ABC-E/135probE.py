
def solve_near(X, Y, K):
    # one time
    if X+Y == K:
        return [(X, Y)]
    
    # three times
    ret = []
    ppx = 1
    ppy = 1
    if K%2 == 1 and (X+Y)%2 != 0:
        dx = K*X//(X+Y)
        dy = K-dx
        X -= dx
        Y -= dy
        ret.append((dx, dy))
        if X < 0:
            X = -X
            ppx = -1
        if Y < 0:
            Y = -Y
            ppy = -1

    # two times
    if X >= Y:
        sx = (X-Y)//2
        sy = K - sx
    else:
        sy = (Y-X)//2
        sx = K - sy
    ret.append((sx * ppx, sy * ppy))
    ret.append(((X-sx) * ppx, (Y-sy) * ppy))
    return ret


def solve(X, Y, K):
    if K%2 == 0 and (X+Y+K)%2 != 0:
        return []
    
    px = 1
    py = 1
    if X < 0:
        px = -1
    if Y < 0:
        py = -1
    
    X *= px
    Y *= py

    ans = []
    while abs(X+Y) >= 2*K:
        dx = K*X//(X+Y)
        dy = K-dx
        ans.append((dx, dy))
        X -= dx
        Y -= dy

    ans += solve_near(X, Y, K)

    ret = []
    x = 0; y = 0
    for dx, dy in ans:
        x += dx*px
        y += dy*py
        ret.append((x, y))
    return ret


def checker(X, Y, K, ans):
    px = 0
    py = 0
    for x, y in ans:
        if abs(x-px) + abs(y-py) != K:
            print("invalid distance", x, y)
            return False
        px = x
        py = y
    if (px, py) != (X, Y):
        print("last point")
        return False
    
    return True
    

if __name__=='__main__':

    K = int(input())
    X, Y = map(int, input().rstrip().split())
    ans = solve(X, Y, K)
    if not ans:
        print(-1)
    else:
        print(len(ans))
        for x, y in solve(X, Y, K):
            print(x, y)
    
    # from random import randint
    # M = 100
    # MAXK = 100000
    # while True:
    #     X = randint(-M, M)
    #     Y = randint(-M, M)
    #     K = randint(1, MAXK)
    #     ans = solve(X, Y, K)
    #     if ans == -1: continue
    #     if not checker(X, Y, K, ans):
    #         print(X, Y, K)
    #         print(ans)
    #         break