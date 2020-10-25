# AOJ CGL_4_A "Convex Hull"

from operator import itemgetter

def ConvexHull(Points):
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

"""
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    Points = [list(map(int, input().split())) for _ in range(N)]
    Qs = ConvexHull(Points)

    min_y = 10**10
    min_x = 10**10
    for i, (x, y) in enumerate(Qs):
        if y < min_y:
            min_y = y
            min_x = x
            min_ind = i
        elif y == min_y and x < min_x:
            min_x = x
            min_ind = i
    Qs = Qs[min_ind:] + Qs[:min_ind]
    print(len(Qs))
    print("\n".join([str(a)+" "+str(b) for a, b in Qs]))
"""