import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

U = "U"
D = "D"
R = "R"
L = "L"

Map = [U, R, D, L]
MAX = 2*10**5+1
INF = 10**18

def solve(N, XYU):
    Xs = [[[] for _ in range(MAX)] for _ in range(4)]
    Ys = [[[] for _ in range(MAX)] for _ in range(4)]
    XpY = [[[] for _ in range(2*MAX)] for _ in range(4)]
    XmY = [[[] for _ in range(2*MAX)] for _ in range(4)]
    for sx, sy, u in XYU:
        x = int(sx)
        y = int(sy)
        c = Map.index(u)
        Xs[c][x].append(y)
        Ys[c][y].append(x)
        XpY[c][x+y].append(x-y)
        XmY[c][x-y].append(x+y)
    
    for c in range(4):
        for i in range(MAX):
            Xs[c][i].sort()
            Ys[c][i].sort()
        for i in range(2*MAX):
            XpY[c][i].sort()
            XmY[c][i].sort()

    ans = INF
    for x in range(MAX):
        if Xs[0][x] and Xs[2][x]:
            ind = 0
            for y in Xs[0][x]:
                while ind < len(Xs[2][x]) and Xs[2][x][ind] <= y: ind += 1
                if ind < len(Xs[2][x]) and Xs[2][x][ind] > y:
                    ans = min(ans, (Xs[2][x][ind]-y)*5)
    for y in range(MAX):
        if Ys[1][y] and Ys[3][y]:
            ind = 0
            for x in Ys[1][y]:
                while ind < len(Ys[3][y]) and Ys[3][y][ind] <= x: ind += 1
                if ind < len(Ys[3][y]) and Ys[3][y][ind] > x:
                    ans = min(ans, (Ys[3][y][ind]-x)*5)
    
    for x in range(MAX):
        for y in Xs[1][x]:
            L1 = XmY[2][x-y]
            i = bisect_right(L1, x+y)
            if i < len(L1):
                ans = min(ans, (L1[i]-(x+y))*5)

            L2 = XpY[0][x+y]
            j = bisect_right(L2, x-y)
            if j < len(L2):
                ans = min(ans, (L2[j]-(x-y))*5)
    
        for y in Xs[3][x]:
            L1 = XpY[2][x+y]
            i = bisect_left(L1, x-y)
            if i > 0:
                ans = min(ans, ((x-y)-L1[i-1])*5)
            
            L2 = XmY[0][x-y]
            j = bisect_left(L2, x+y)
            if j > 0:
                ans = min(ans, ((x+y)-L2[j-1])*5)
    
    return ans if ans != INF else "SAFE"

if __name__=='__main__':
    N = int(input())
    XYU = [list(map(str, input().rstrip().split())) for _ in range(N)]
    print(solve(N, XYU))