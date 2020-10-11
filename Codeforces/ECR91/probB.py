import sys
input = sys.stdin.readline
from operator import itemgetter

Q = int(input())
for _ in range(Q):
    S = input().rstrip()
    dic = {"R": 0, "S":0, "P":0}
    for s in S:
        dic[s] += 1
    P = sorted(list(dic.items()), key=itemgetter(1))
    W = P[-1][0]
    if W == "R":
        E = "P"
    elif W == "S":
        E = "R"
    else:
        E = "S"
    print(E*len(S))