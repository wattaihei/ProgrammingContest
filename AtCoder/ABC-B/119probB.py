N = int(input())


money = 0
for _ in range(N):
    xs, u = map(str, input().split()) # 横に2個
    x = float(xs)
    if u == 'BTC':
        money += x * 380000.0
    else:
        money += x

print(money)