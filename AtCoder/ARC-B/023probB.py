from operator import itemgetter

R, C, D = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(R)]

scores = []
for r in range(R):
    for c in range(C):
        scores.append((r, c, state[r][c]))

scores.sort(reverse=True, key=itemgetter(2))

for r, c, score in scores:
    if r+c <= D and (D-r-c)%2 == 0:
        print(score)
        break