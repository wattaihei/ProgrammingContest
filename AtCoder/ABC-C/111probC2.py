import collections
from operator import itemgetter

N = int(input())

up = []
down = []
for i, v in enumerate(list(map(int, input().split()))):
    if i % 2 == 0:
        up.append(v)
    else:
        down.append(v)

ud = collections.Counter(up)
dd = collections.Counter(down)

ul = []
for u, c in ud.items():
    ul.append([u, c])
dl = []
for d, c in dd.items():
    dl.append([d, c])

ul.sort(key=itemgetter(1), reverse=True)
dl.sort(key=itemgetter(1), reverse=True)

if ul[0][0] != dl[0][0]:
    print(N - ul[0][1] - dl[0][1])
elif len(ul) == 1 and len(dl) > 1:
    print(N - ul[0][1] - dl[1][1])
elif len(ul) > 1 and len(dl) == 1:
    print(N - ul[1][1] - dl[0][1])
elif len(ul) == 1 and len(dl) == 1:
    print(N//2)
else:
    print(N - max(ul[0][1]+dl[1][1], ul[1][1]+dl[0][1]))