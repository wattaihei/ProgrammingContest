N, M, X, Y = map(int, input().split()) # 横に2個
Xs = list(map(int, input().split()))
Ys = list(map(int, input().split()))

Xs.sort()
Ys.sort()

if max(Xs[-1], X) < min(Ys[0], Y):
    ans = 'No War'
else:
    ans = 'War'

print(ans)