from collections import Counter

H, W = map(int, input().split())

SS = []
for _  in range(H):
    for a in list(input()):
        SS.append(a)

S = Counter(SS)


cwh = 0
ok = True
corner = 0
for c in S.values():
    if c >= 4:
        corner += c // 4
        c = c % 4
    if c == 0:
        continue
    elif c == 3:
        if H % 2 == 1 and W % 2 == 1:
            cwh += 1
        else:
            ok = False
    elif c == 1:
        if H % 2 == 1 and W % 2 == 1:
            cwh += 1
        else:
            ok = False

if cwh >= 2 or not ok:
    ans = 'No'
else:
    ans = 'Yes'
    if corner < (W//2)*(H//2):
            ans = 'No'
    if H % 2 == 1 and W % 2 == 1:
        if cwh != 1:
            ans = 'No'
print(ans)
