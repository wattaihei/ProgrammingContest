import numpy as np


N = int(input())
dis = np.zeros((N, N), dtype=int)
for i in range(N-1):
    u, v, w = map(int, input().split())
    dis[u-1, v-1] = w
print(dis)


while np.count_nonzero(dis) != N**2 - N:

    dis = np.triu(dis, k=1) + np.triu(dis.T, k=1)
    dis = dis + dis.T

def coloring(point, color):
    if color[point-1]:
        pass