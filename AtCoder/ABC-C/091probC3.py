from operator import itemgetter

N = int(input())
Red = [list(map(int, input().split())) for _ in range(N)]
Blue = [list(map(int, input().split())) for _ in range(N)]

Red.sort(key=itemgetter(0), reverse=True)
checked = [False for _ in range(N)]

c = 0
for rx, ry in Red:
    P = []
    for i, (bx, by) in enumerate(Blue):
        if bx > rx and by > ry and not checked[i]:
            P.append((i, by))
    if P:
        P.sort(key=itemgetter(1))
        ip, _ = P[0]
        checked[ip] = True
        c += 1

print(c)