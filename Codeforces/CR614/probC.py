import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(Q)]

row1 = set()
row2 = set()
close = set()
for r, w in Query:
    if r == 1:
        if w in row1:
            row1.remove(w)
            if w in close:
                close.remove(w)
        else:
            row1.add(w)
            nexts = [w-1, w, w+1]
            for n in nexts:
                if n in row2:
                    close.add(w)
                    break
    else:
        if w in row2:
            row2.remove(w)
            prob = [w-1, w, w+1]
            can1 = []
            for p in prob:
                if p in row1:
                    can1.append(p)
            for p in can1:
                canrem = True
                for n in [p-1, p, p+1]:
                    if n != w and n in row2:
                        canrem = False
                if canrem:
                    close.remove(p)
        else:
            row2.add(w)
            for n in [w-1, w, w+1]:
                if n in row1:
                    close.add(n)
    print("Yes" if not close else "No")

