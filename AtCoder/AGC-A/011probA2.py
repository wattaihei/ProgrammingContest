N, C, K = map(int, input().split()) # 横に2個
T = [int(input()) for _ in range(N)]

T.sort()

first = True
ans = 0
peo = 0
limit = T[-1]
for t in T:
    if peo == C or t > limit:
        ans += 1
        first = True
    if first:
        limit = t + K
        peo = 1
        first = False
    elif t <= limit:
        peo += 1

if peo > 0:
    ans += 1

print(ans)