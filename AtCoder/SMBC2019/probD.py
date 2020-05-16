from bisect import bisect_right

import sys
input = sys.stdin.readline

N = int(input())
S = input()

dic = {}
for i in range(N):
    n = int(S[i])
    if not n in dic.keys():
        dic[n] = [i]
    else:
        dic[n].append(i)

c = 0
for k1 in range(10):
    if not k1 in dic.keys():
        continue
    i1 = dic[k1][0]
    for k2 in range(10):
        if not k2 in dic.keys():
            continue
        j2 = bisect_right(dic[k2], i1)
        if j2 == len(dic[k2]):
            continue
        i2 = dic[k2][j2]
        for k3 in range(10):
            if not k3 in dic.keys():
                continue
            j3 = bisect_right(dic[k3], i2)
            if j3 == len(dic[k3]): continue
            c += 1

print(c)