from operator import itemgetter

A = [[int(a[0]), a[1]] for a in list(map(str, input().split()))]

D = {}
for a in A:
    if not a[1] in D.keys():
        D[a[1]] = [a[0]]
    else:
        D[a[1]].append(a[0])

ans = 2
for d in D.values():
    if len(d) == 1:
        continue
    elif len(d) == 2:
        if d[0] == d[1] or abs(d[0]-d[1]) == 1 or abs(d[0]-d[1]) == 2:
            ans = min(ans, 1)
    else:
        d.sort()
        if d[0] == d[2] or (abs(d[0]-d[1]) == 1 and abs(d[2]-d[1]) == 1):
            ans = 0
        elif d[0] == d[1] or d[1] == d[2] or abs(d[0]-d[1]) == 1 or abs(d[2]-d[1]) == 1 or abs(d[0]-d[1]) == 2 or abs(d[2]-d[1]) == 2:
            ans = min(ans, 1)

print(ans)
