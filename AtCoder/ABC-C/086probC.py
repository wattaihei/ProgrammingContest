N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

pt, px, py = [0, 0, 0]
ans = 'Yes'
for t, x, y in XY:
    lim = t - pt
    need = abs(x-px) + abs(y-py)
    if lim < need or (lim-need)%2==1:
        ans = 'No'
        break
    pt, px, py = t, x, y

print(ans)