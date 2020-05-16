from operator import itemgetter

N = int(input())
score = []
for _ in range(N):
    a, b = map(int, input().split())
    score.append((a, b, a+b))

score.sort(key=itemgetter(2), reverse=True)

ans = 0
for i in range(N):
    if i%2 == 0:
        ans += score[i][0]
    else:
        ans -= score[i][1]
print(ans)