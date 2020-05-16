from operator import itemgetter
from bisect import bisect_left, bisect_right
import heapq as hp
import sys
input = sys.stdin.readline

#import numpy as np
#import matplotlib.pyplot as plt

'''
def graph_ABC065D(N, max_xy):
    print(N)
    XY = []
    for _ in range(N):
        xi = np.random.randint(0, max_xy)
        yi = np.random.randint(0, max_xy)
        XY.append([xi, yi])
        print(xi, yi)
    return N, XY


def plot(N, XY, max_xy):
    X, Y = zip(*XY)
    plt.scatter(X, Y)
    plt.grid(b=True)
    plt.xlim((0, max_xy))
    plt.ylim((0, max_xy))
    plt.xticks(np.arange(0, max_xy, 1))
    plt.yticks(np.arange(0, max_xy, 1))
    plt.show()
'''

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    Xs = []
    Ys = []
    for i, (x, y) in enumerate(XY):
        Xs.append((i, x))
        Ys.append((i, y))
    Xs.sort(key=itemgetter(1))
    Ys.sort(key=itemgetter(1))

    Ix, X = zip(*Xs)
    Iy, Y = zip(*Ys)
    # Ix, Iy are indexes of XY
    Rx = [None]*N
    Ry = [None]*N
    for i, (ix, iy) in enumerate(zip(Ix, Iy)):
        Rx[ix] = i
        Ry[iy] = i

    # take nearest 4s
    graph = [[] for _ in range(N)]
    for i, (x, y) in enumerate(XY):
        nexts = set()
        ix = Rx[i]
        if ix != 0:
            nexts.add(Ix[ix-1])
        if ix != N-1:
            nexts.add(Ix[ix+1])
        
        iy = Ry[i]
        if iy != 0:
            nexts.add(Iy[iy-1])
        if iy != N-1:
            nexts.add(Iy[iy+1])
        
        for n in nexts:
            d = min(abs(XY[n][0]-XY[i][0]), abs(XY[n][1]-XY[i][1]))
            graph[i].append((d, n))



    checked = [False for _ in range(N)]
    checked[0] = True 
    q = [] # しまっていく優先度付きキュー
    for d, n in graph[0]:
        hp.heappush(q, (d, n))
    ans = 0

    #print(graph)
    while q:
        nd, np = hp.heappop(q) # 一番距離が近いものを取ってくる
        #print(nd, np, q)
        if checked[np]: # 追加した後の残骸は見ない
            continue
        ans += nd
        #print(ans)
        checked[np] = True
        for d, p in graph[np]:
            if not checked[p]:
                hp.heappush(q, (d, p))

    print(ans)
            

if __name__ == "__main__":
    #print('input data')
    #N = 9
    #max_xy = 20
    #N, XY = graph_ABC065D(N, max_xy)
    #print('answer')
    #main(N, XY)
    #plot(N, XY, max_xy)

    main()
