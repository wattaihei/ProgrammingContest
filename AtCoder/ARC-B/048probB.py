import sys
input = sys.stdin.readline

from operator import itemgetter

N = int(input())
RH = [list(map(int, input().split())) for _ in range(N)]

dic = {}
for i, (r, h) in enumerate(RH):
    if not r in dic.keys():
        dic[r] = [i]
    else:
        dic[r].append(i)

A = sorted(dic.items(), key=itemgetter(0))
ans = [[0, 0, 0] for _ in range(N)]

P = 0
for _, List in A:
    gcp = [0, 0, 0]
    for i in List:
        gcp[RH[i][1]-1] += 1
    for i in List:
        ans[i][0] += P
        ans[i][1] += N - P - len(List)
        te = RH[i][1]
        if te == 1:
            ans[i][0] += gcp[1]
            ans[i][1] += gcp[2]
            ans[i][2] += gcp[0] - 1
        elif te == 2:
            ans[i][0] += gcp[2]
            ans[i][1] += gcp[0]
            ans[i][2] += gcp[1] - 1
        else:
            ans[i][0] += gcp[0]
            ans[i][1] += gcp[1]
            ans[i][2] += gcp[2] - 1
    P += len(List)

for i, j, k in ans:
    print(i, j, k)