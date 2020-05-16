from collections import Counter

L, R = map(int, input().split())

update = False
for i in range(L, R+1):
    a = list(str(i))
    B = Counter(a)
    ok = True
    for c in B.values():
        if c != 1:
            ok = False
    if ok:
        update = True
        print(i)
        break

if not update:
    print(-1)