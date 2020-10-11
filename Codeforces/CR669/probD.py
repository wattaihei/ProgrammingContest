import sys
input = sys.stdin.buffer.readline

from collections import deque

# AOJ CGL_4_A "Convex Hull"

from operator import itemgetter

INF = 10**18

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

def main():
    N = int(input())
    A = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    Points = []
    for i, a in enumerate(A):
        Points.append((i, a))
    
    Qs = ConvexHull(Points)
    for i in range(len(Qs)):
        i1, a1 = Qs[i-1]
        i2, a2 = Qs[i]
        if i1 < i2:
            if a1 > a2:
                while i1 + 1 < i2 and A[i2-1] <= a1:
                    i2 -= 1
                if i1 + 1 < i2:
                    graph[i1].append((i2, 1))
            else:
                while i1 + 1 < i2 and A[i1+1] <= a2:
                    i1 += 1
                if i1 + 1 < i2:
                    graph[i1].append((i2, 1))
        else:
            if a1 > a2:
                while i2 + 1 < i1 and A[i1-1] >= a2:
                    i1 -= 1
                if i2 + 1 < i1:
                    graph[i2].append((i1, 1))
            else:
                while i2 + 1 < i1 and A[i2+1] >= a1:
                    i2 += 1
                if i2 + 1 < i1:
                    graph[i2].append((i1, 1))
        

    
    
    # Points.sort(key=itemgetter(1))
    # Points.sort()
    # Used = [False]*N
    # stack = []
    # for a, i in Points:
    #     if Used[i]: continue
    #     if stack:
    #         j = stack.pop()
    #         l, m = min(i, j), max(i, j)
    #         for k in range(l, m+1):
    #             Used[k] = True
    #         graph[l].append((m, 1))
    #     stack.append(i)

    # # Points.sort(key=itemgetter(1))
    # Points.sort(reverse=True)
    # Used = [False]*N
    # stack = []
    # for a, i in Points:
    #     if Used[i]: continue
    #     if stack:
    #         j = stack.pop()
    #         l, m = min(i, j), max(i, j)
    #         for k in range(l, m+1):
    #             Used[k] = True
    #         graph[l].append((m, 1))
    #     stack.append(i)
    
    
    for i in range(N-1):
        graph[i].append((i+1, 1))
        graph[i+1].append((i, 0))
    
    q = deque()
    q.append(0)
    D = [INF]*N
    D[0] = 0
    while q:
        p = q.pop()
        for np, d in graph[p]:
            if D[np] > D[p] + d:
                D[np] = D[p] + d
                if d == 0:
                    q.append(np)
                else:
                    q.appendleft(np)
    print(D[N-1])
            
    

if __name__ == "__main__":
    main()