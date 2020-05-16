import math
from operator import itemgetter

def scan(Points):
    N = Points
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


def distances(Points):
    L = len(Points)
    d = 0
    for i in range(L):
        x1, y1 = Points[i-1]
        x2, y2 = Points[i]
        d += math.sqrt((x1-x2)**2+(y1-y2)**2)
    return d


import sys
input = sys.stdin.readline


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

P_a = scan(A)
P_b = scan(B)
d1 = distances(P_a)
d2 = distances(P_b)
print(d2/d1)