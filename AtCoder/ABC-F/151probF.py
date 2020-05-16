import sys
input = sys.stdin.readline

# AOJ CGL_4_A "Convex Hull"

from operator import itemgetter

def scan(Points):
    Points.sort(key=itemgetter(1))
    Points.sort(key=itemgetter(0))

    k = 0
    Qs = []
    for x, y in Points:
        while len(Qs) > 1:
            x1, y1 = Qs[-1]
            x2, y2 = Qs[-2]
            if (y1-y)*(x-x2) > (y-y2)*(x1-x):
                Qs.pop()
            else:
                break
        Qs.append((x, y))
        
    t = len(Qs)
    Qs.pop()
    for x, y in reversed(Points):
        while len(Qs) > t:
            x1, y1 = Qs[-1]
            x2, y2 = Qs[-2]
            if (y1-y)*(x-x2) > (y-y2)*(x1-x):
                Qs.pop()
            else:
                break
        Qs.append((x, y))
    Qs.pop()

    return Qs

import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def main():
    if N == 2:
        x1, y1 = XY[0]
        x2, y2 = XY[1]
        d = math.sqrt((x1-x2)**2+(y1-y2)**2)
        print(d/2)
        return
    outerpoints = scan(XY)

    min2 = 10**16
    for i in range(N-1):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            px, py = (x1+x2)/2, (y1+y2)/2
            r = math.sqrt((px-x1)**2+(py-y1)**2)
            using = [(x1, y1), (x2, y2)]
            ok = True
            for ox, oy in outerpoints:
                if (ox, oy) in using:
                    continue
                if math.sqrt((ox-px)**2+(oy-py)**2) > r:
                    ok = False
                    break
            if ok:
                min2 = min(min2, r)
    
                
    min3 = 10**16
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                a, b = XY[i]
                c, d = XY[j]
                e, f = XY[k]
                if (2*(e-a)*(b-d)-2*(c-a)*(b-f)) == 0:
                    px = (max([a, c, e])+min([a, c, e]))/2
                    py = (max([b, d, f])+min([b, d, f]))/2
                else:
                    py = ((e-a)*(a**2+b**2-c**2-d**2) - (c-a)*(a**2+b**2-e**2-f**2)) / (2*(e-a)*(b-d)-2*(c-a)*(b-f))
                    if c != a:
                        px = (2*(b-d)*py-a**2-b**2+c**2+d**2)/(2*(c-a))
                    else:
                        px = (2*(b-f)*py-a**2-b**2+e**2+f**2)/(2*(e-a))
                r = math.sqrt((px-a)**2+(py-b)**2)
                using = [(a, b), (c, d), (e, f)]
                ok = True
                for ox, oy in outerpoints:
                    if (ox, oy) in using:
                        continue
                    if math.sqrt((ox-px)**2+(oy-py)**2) > r:
                        ok = False
                        break
                if ok:
                    min3 = min(min3, r)
    print(min(min2, min3))
    return


if __name__ == "__main__":
    main()