from operator import itemgetter
import numpy as np
import scipy.stats as stats

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

xy = sorted(xy, key=itemgetter(1))
xy = sorted(xy, key=itemgetter(0))

print(xy)

xy_a = np.array(xy)

x1 = xy_a[:, 0]
x2 = xy_a[:, 1]

def calc_mode(xi):
    dl_a = np.diff(xi)
    stats_c = stats.mode(dl_a)
    maxcount = stats_c[1][0]
    max = []
    i = 0
    while stats_c[1][i] == maxcount:
        max.append(stats_c[0][i])
        i += 1
        if i > len(stats_c[1])-1:
            break
    return max

max0 = calc_mode(x1)
max1 = calc_mode(x2)

p0 = xy_a[0, 0]
q0 = xy_a[0, 1]

print(max0, max1)

Cost = N
for p in max0:
    for q in max1:
        deltaxy = []
        for i in range(N):
            deltaxy.append([p0+i*p, q0+i*q])
        delta_array = xy_a[:-1, :]
        cost = N - np.count_nonzero(np.all(delta_array - xy_a == 0, axis=1)) + 1
        if cost < Cost:
            Cost = cost

print(Cost)