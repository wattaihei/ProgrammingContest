from operator import itemgetter

N, T = map(int, input().split()) # 横に2個
ct = [list(map(int, input().split())) for _ in range(N)]

ans = -1
ct.sort(key=itemgetter(1))
for i, c in enumerate(ct):
    if c[1] > T:
        break
    if i == 0:
        ans = c[0]
        continue
    ans = min(ans, c[0])

if ans == -1:
    print('TLE')
else:
    print(ans)