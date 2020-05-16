from bisect import bisect_left

import sys
input = sys.stdin.readline

N = int(input())
Ss = [list(input()) for _ in range(N)]

Alp = [chr(i) for i in range(65, 65+26)] + [chr(i) for i in range(97, 97+26)]


P = []
for S in Ss:
    dic = {}
    for a in Alp:
        dic[a] = []
    for i, s in enumerate(S):
        dic[s].append(i)
    P.append(dic)

for s1 in Alp:
    for s2 in Alp:
        for s3 in Alp:
            
