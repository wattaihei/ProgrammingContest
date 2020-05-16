import sys
input = sys.stdin.readline

x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, T = map(int, input().split())

MAX = max(xs, ys) + T + 1
C = [(x0, y0)]
while True:
    x = ax*C[-1][0] + bx
    y = ay*C[-1][1] + by
    if x > MAX or y > MAX:
        break
    C.append((x, y))

ans = 0
for i, (xt, yt) in enumerate(C):
    D = abs(xs-xt) + abs(ys-yt)
    if D > T:
        continue
    ind = i
    while ind > 0:
        d = abs(C[ind][0]-C[ind-1][0]) + abs(C[ind][1]-C[ind-1][1])
        if D + d > T:
            break
        D += d
        ind -= 1
    ans = max(ans, i-ind+1)

    D = abs(xs-xt) + abs(ys-yt)
    ind = i
    while ind < len(C)-1:
        d = abs(C[ind][0]-C[ind+1][0]) + abs(C[ind][1]-C[ind+1][1])
        if D + d > T:
            break
        D += d
        ind += 1
    ans = max(ans, ind-i+1)

print(ans)