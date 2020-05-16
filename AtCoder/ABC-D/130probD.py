import numpy as np
from bisect import bisect_left

def main():
    N, K = map(int, input().split()) # 横に2個
    a = list(map(int, input().split())) # １行に別れてるとき
    bl = [0]
    for i in range(N):
        bl.append(a[i]+bl[i])
    b = np.array(bl)

    c = 0
    for i in range(N):
        c += N - i - bisect_left(b[i+1:] - b[i], K)
    print(c)

if __name__=='__main__':
    try:
        main()
    except MemoryError as e:
        print(e)