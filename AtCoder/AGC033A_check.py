from queue import Queue
import time
import sys
from operator import itemgetter
input = sys.stdin.readline

import numpy as np
import matplotlib.pyplot as plt

B = int(1E8)

def main(H, W):
    t0 = time.time()

    sample = []
    for _ in range(H):
        S = ''
        for _ in range(W):
            s = np.random.choice(['.', '#'], p=[0.9, 0.1])
            S += s
        sample.append(S)
    
    l = 0
    q = Queue()
    checked = []
    for h in range(H):
        S = sample[h]
        L = []
        for w in range(W):
            if S[w] == '#':
                l += 1
                L.append(True)
                q.put(B*h + w)
            else:
                L.append(False)
        checked.append(L)

    t1 = time.time()

    Next = [[[] for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if h != 0:
                Next[h][w].append(B*(h-1) + w)
            if h != H-1:
                Next[h][w].append(B*(h+1) + w)
            if w != 0:
                Next[h][w].append(B*h + w-1)
            if w != W-1:
                Next[h][w].append(B*h + w+1)
    
    t2 = time.time()
    print('Next list made', t2-t1)

    c = -1
    for _ in range(H+W+2):
        if l == 0:
            break
        nl = 0
        for _ in range(l):
            hw = q.get()
            h, w = hw//B, hw%B
            for nhw in Next[h][w]:
                nh, nw = nhw//B, nhw%B
                if not checked[nh][nw]:
                    q.put(B*nh + nw)
                    checked[nh][nw] = True
                    nl += 1
        l = nl
        c += 1
    
    t3 = time.time()
    print('bfs finished', t3-t2)
    print('all time', t3-t1)

    print(c)
    return t3-t2


if __name__ == "__main__":
    XY = []
    for i in range(11):
        for j in range(11):
            print('H = ', 2**i, ', W = ', 2**j+1)
            bfs_time = main(2**i, 2**j+1)
            grid_size = 2**i * (2**j+1)
            XY.append([grid_size, bfs_time])
    XY.sort(key=itemgetter(0))
    x = []
    y = []
    for a, b in XY:
        x.append(a)
        y.append(b)
    plt.plot(x, y, color='blue', label='data')

    y1 = []
    for ix in x:
        y1.append(ix - x[-1] + y[-1])

    #plt.plot(x, y1, color='green', label='O(N)')
    #plt.plot(x1, y2, color='yellow', label='O(N^2)')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('grid size')
    plt.ylabel('time [s]')
    plt.title('BFS by Python (AGC033-A)')

    plt.vlines(1000000, 0.0001, 10, colors='orange', label='largest grid')
    plt.hlines(1, 1, 10000000, colors='yellow', label='time limit')
    plt.legend()
    plt.show()