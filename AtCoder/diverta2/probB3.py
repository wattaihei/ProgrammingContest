from operator import itemgetter

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort(key=itemgetter(1))
XY.sort(key=itemgetter(0))

ans = N
for i in range(N-1):
    for j in range(i+1, N):
        p = XY[j][0] - XY[i][0]
        q = XY[j][1] - XY[i][1]
        cost1 = N
        cost2 = N
        for x, y in XY:
            if [x+p, y+q] in XY:
                cost1 -= 1
            if [x-p, y-q] in XY:
                cost2 -= 1
        ans = min([ans, cost1, cost2])
print(ans)