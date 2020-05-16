import sys
input = sys.stdin.readline

N = int(input())
Bs = []
Cs = []
XY = []
for _ in range(N):
    x0, y0 = map(int, input().split())
    Bs.append(-x0+y0)
    Cs.append(x0+y0)
    XY.append((x0, y0))

Bs.sort()
Cs.sort()
up1 = Bs[0]
up2 = Bs[-1]
do1 = Cs[0]
do2 = Cs[-1]

Probs = [((do2-up2)//2, (do1+up2)//2), ((do1-up1)//2, (do2+up1)//2), ((do1-up1)//2, (do1+up2)//2), ((do2-up2)//2, (do2+up1)//2)]
for px, py in Probs:
    d = -1
    ok = True
    for x, y in XY:
        if d == -1:
            d = abs(px-x) + abs(py-y)
        elif abs(px-x) + abs(py-y) != d:
            ok = False
            break
    if ok:
        print(px, py)
        break