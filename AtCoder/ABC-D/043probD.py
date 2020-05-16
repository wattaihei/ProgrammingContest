S = list(input())

dic = {}
for i, s in enumerate(S):
    if not s in dic.keys():
        dic[s] = [i]
    else:
        dic[s].append(i)

ok = False
for v in dic.values():
    x = len(v)
    if x < 2:
        continue
    B = [None]*x
    for i in range(x):
        B[i] = v[i] - 2*i
    l = 0
    for r in range(1, x):
        if B[l] >= B[r]:
            ok = True
            L, R = v[l]+1, v[r]+1
            break
        else:
            l = r
    if ok:
        break

if not ok:
    print(-1, -1)
else:
    print(L, R)