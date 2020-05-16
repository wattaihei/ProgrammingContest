N = int(input())
W = [input() for _ in range(N)]
checked = []

pre = W[0][0]
ok = True
for w in W:
    if w[0] != pre[-1] or w in checked:
        ok = False
        break
    pre = w
    checked.append(w)

if ok:
    print('Yes')
else:
    print('No')