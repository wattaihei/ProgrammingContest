import collections

n = int(input())
v = list(map(int, input().split()))

vdic = collections.Counter(v)

vlist = []
over = False
for num, c in vdic.items():
    if c > n//2:
        over = True
    vlist.append(abs(c - n//2))

vlist.sort()
if len(vlist) == 1:
    print(vlist[0])
elif over:
    print(vlist[1])
else:
    print(vlist[0]+vlist[1])